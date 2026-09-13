import os
import re
import sys

# Patterns that can indicate hardcoded secrets
SECRET_PATTERNS = [
    r"AKIA[0-9A-Z]{16}",                         # AWS Access Key
    r"aws_secret_access_key\s*=\s*[\"'][^\"']+[\"']",
    r"password\s*=\s*[\"'][^\"']+[\"']",
    r"secret\s*=\s*[\"'][^\"']+[\"']",
]

# Files/folders we don't need to scan
EXCLUDED_DIRS = {
    "venv",
    ".git",
    "__pycache__"
}

EXCLUDED_FILES = {
    "sec_scan.py"
}


def scan_file(file_path):
    """Scan one file for possible secrets."""

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            content = file.read()
    except Exception:
        return []

    findings = []

    for pattern in SECRET_PATTERNS:
        if re.search(pattern, content, re.IGNORECASE):
            findings.append(pattern)

    return findings


def scan_project():
    """Scan the project directory."""

    secrets_found = []

    for root, dirs, files in os.walk("."):

        # Don't enter excluded directories
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]

        for filename in files:

            if filename in EXCLUDED_FILES:
                continue

            file_path = os.path.join(root, filename)

            findings = scan_file(file_path)

            if findings:
                secrets_found.append(file_path)

    return secrets_found


if __name__ == "__main__":

    print("🔍 Starting security scan...")

    results = scan_project()

    if results:
        print("\n❌ SECURITY SCAN FAILED!")
        print("Possible secrets found in:")

        for file in results:
            print(f"   🚨 {file}")

        print("\nCommit/operation blocked.")
        sys.exit(1)

    print("✅ Security scan passed!")
    print("No hardcoded secrets detected.")
    sys.exit(0)