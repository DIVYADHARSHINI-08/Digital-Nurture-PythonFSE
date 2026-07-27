# Week 7 – Cloud Deployment

## Overview

This module introduces the fundamentals of cloud computing and modern deployment practices using AWS, Microsoft Azure, and Google Cloud Platform. It also covers containerization with Docker, Kubernetes basics, CI/CD pipelines, and cloud security concepts used in real-world software development.

---

# Learning Objectives

After completing this module, I was able to:

* Understand cloud computing fundamentals.
* Deploy containerized applications to cloud platforms.
* Configure CI/CD pipelines for automated build and deployment.
* Understand cloud compute, storage, and managed database services.
* Write Dockerfiles and build Docker images.
* Run Docker containers locally.
* Deploy applications using cloud free-tier services.
* Provision cloud storage resources.
* Configure IAM permissions for secure access.
* Understand Kubernetes architecture and deployment concepts.
* Learn cloud security and monitoring best practices.

---

# Topics Covered

## 1. Amazon Web Services (AWS)

### Services Learned

* EC2
* S3
* RDS
* IAM
* Elastic Beanstalk
* AWS Lambda
* CloudWatch
* AWS CLI

### Key Takeaways

* EC2 provides scalable virtual machines.
* S3 offers secure object storage.
* IAM manages authentication and authorization.
* Elastic Beanstalk simplifies application deployment.
* Lambda enables serverless computing.
* CloudWatch provides monitoring and logging.

---

## 2. Microsoft Azure

### Services Learned

* Azure App Service
* Azure SQL
* Blob Storage
* Azure Functions
* Azure DevOps
* Application Insights

### Key Takeaways

* Azure App Service hosts web applications.
* Blob Storage stores unstructured data.
* Azure SQL provides managed databases.
* Azure Functions support serverless execution.
* Azure DevOps enables CI/CD and project management.

---

## 3. Google Cloud Platform (GCP)

### Services Learned

* Compute Engine
* Cloud Run
* Cloud Storage
* Cloud SQL
* Cloud Functions
* gcloud CLI

### Key Takeaways

* Compute Engine provides virtual machines.
* Cloud Run deploys containerized applications.
* Cloud Storage manages scalable object storage.
* Cloud SQL offers managed relational databases.
* Cloud Functions execute event-driven workloads.

---

## 4. Docker & Containerization

### Concepts Learned

* Docker Architecture
* Docker Images
* Containers
* Dockerfile
* Docker Compose
* Multi-stage Builds
* Container Best Practices

### Common Docker Commands

```bash
docker build -t myapp .
docker run -p 8080:8080 myapp
docker ps
docker stop <container-id>
docker images
docker compose up
```

### Key Takeaways

* Docker packages applications with dependencies.
* Containers provide consistent execution across environments.
* Docker Compose manages multi-container applications.

---

## 5. Kubernetes Basics

### Concepts Learned

* Pods
* Deployments
* Services
* ConfigMaps
* Secrets
* kubectl Basics
* Managed Kubernetes Services

### Key Takeaways

* Pods are the smallest deployable Kubernetes units.
* Deployments manage application replicas.
* Services expose applications to users.
* ConfigMaps and Secrets manage configuration securely.

---

## 6. CI/CD Pipelines

### Concepts Learned

* Continuous Integration
* Continuous Deployment
* GitHub Actions
* Azure Pipelines
* Build Stage
* Test Stage
* Deployment Stage
* Environment Promotion

### Key Takeaways

* CI/CD automates software delivery.
* Automated testing improves reliability.
* GitHub Actions simplifies deployment workflows.

---

## 7. Cloud Security & Monitoring

### Concepts Learned

* IAM Principles
* Secrets Management
* HTTPS/TLS
* Logging
* Monitoring
* Cost Management

### Key Takeaways

* IAM protects cloud resources.
* Secrets should never be stored in source code.
* Monitoring helps identify system issues early.
* Cost optimization is important in cloud environments.

---

# Practical Activities

During this module, the following activities were practiced:

* Created Dockerfiles.
* Built Docker images.
* Ran containers locally.
* Deployed applications to cloud platforms.
* Configured GitHub Actions workflows.
* Built automated CI/CD pipelines.
* Provisioned cloud storage resources.
* Uploaded files securely.
* Configured IAM permissions.
* Explored Kubernetes deployment concepts.

---

# Skills Gained

* Cloud Computing
* AWS Fundamentals
* Microsoft Azure Basics
* Google Cloud Platform Basics
* Docker
* Containerization
* Kubernetes Fundamentals
* CI/CD Pipelines
* GitHub Actions
* Cloud Deployment
* IAM
* Cloud Security
* Monitoring & Logging

---

# Conclusion

This module provided practical knowledge of cloud deployment, containerization, Kubernetes, CI/CD automation, and cloud security. These concepts are essential for building, deploying, and maintaining scalable modern applications in production environments.
