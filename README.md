# AWS Security Gate & Auto-Deployment Pipeline

A DevOps project that demonstrates secure application deployment using
Git, GitHub Actions, Docker, Amazon ECR, and Amazon ECS Fargate.

## Project Overview

This project deploys a FastAPI application to AWS using a containerized
CI/CD workflow.

Before code is committed, a security scanner checks the project for
possible hardcoded secrets. The application is then built into a Docker
image and pushed to Amazon ECR. Amazon ECS Fargate runs the container
as a service.

## Architecture

Developer
    ↓
Git Pre-Commit Security Scan
    ↓
GitHub
    ↓
GitHub Actions
    ↓
Docker Build
    ↓
Amazon ECR
    ↓
Amazon ECS
    ↓
AWS Fargate
    ↓
FastAPI Application

## Technologies Used

- Python
- FastAPI
- Git
- GitHub
- GitHub Actions
- Docker
- Amazon ECR
- Amazon ECS
- AWS Fargate
- AWS IAM
- Amazon VPC
- Security Groups

## Security

A custom Python security scanner checks the project before commits
and blocks commits when potential hardcoded secrets are detected.

## Deployment

The application is containerized using Docker and pushed to Amazon ECR.

Amazon ECS Fargate runs the Docker container using an ECS Task Definition
and ECS Service.

## Application

The FastAPI application exposes an API endpoint that confirms the
application is running successfully.

Example response:

{
    "message": "AWS Security Gate Application is running",
    "status": "success"
}

## AWS Deployment

- ECS Cluster: aws-security-gate-cluster
- ECS Service: aws-security-gate-service
- ECS Task Definition: aws-security-gate-task
- ECR Repository: aws-security-gate
- Launch Type: Fargate
- Container Port: 8000

## Project Outcome

The application was successfully containerized and deployed to AWS ECS
Fargate and accessed through a public endpoint.