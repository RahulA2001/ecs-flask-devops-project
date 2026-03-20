**🚀 Production-Ready Flask Deployment on AWS ECS (Fargate) with CI/CD**
📌 Project Summary

Designed and implemented a containerized microservice deployment pipeline using AWS and GitHub Actions. This project demonstrates real-world DevOps practices including:

Automated CI/CD pipeline

Immutable infrastructure deployment

Container orchestration using serverless compute (Fargate)

Version-controlled releases with rollback capability

🧠 Key Highlights (Resume Points)

Built and deployed a Dockerized Flask application on AWS ECS (Fargate)

Implemented end-to-end CI/CD pipeline using GitHub Actions

Enabled zero-downtime rolling deployments

Designed versioned image strategy using Git commit SHA

Integrated Amazon ECR for container registry

Configured CloudWatch logging for observability

Implemented manual rollback mechanism via workflow inputs

Followed Infrastructure-as-Code principles with ECS task definitions

🏗️ Architecture Overview
Developer Push → GitHub Actions → Docker Build → Amazon ECR → ECS Fargate → Application Deployment
                                              ↓
                                      CloudWatch Logs
⚙️ Tech Stack
Category	Tools / Services
Cloud	AWS ECS (Fargate), ECR, CloudWatch
CI/CD	GitHub Actions
Containerization	Docker
Backend	Python (Flask)
IaC	ECS Task Definition (JSON)
📁 Project Structure
.
├── app.py                  # Flask application
├── Dockerfile              # Container definition
├── ecs-task-def.json       # ECS task definition (IaC)
└── .github/workflows/
    └── deploy.yml          # CI/CD pipeline
🐳 Containerization

Lightweight base image (python:3.9-slim)

Stateless container design

Exposes port 80 for HTTP traffic

Build & Run Locally
docker build -t ecs-app .
docker run -p 80:80 ecs-app
☁️ AWS Deployment
ECS Configuration

Launch Type: Fargate (Serverless)

CPU: 512

Memory: 1024

Network Mode: awsvpc

Logging: CloudWatch (awslogs driver)

Container

Image hosted in Amazon ECR

Port mapped: 80

⚙️ CI/CD Pipeline (GitHub Actions)
🔄 Workflow Capabilities

Triggered on push to main

Builds Docker image

Tags image with:

latest

Git commit SHA (versioning)

Pushes image to ECR

Updates ECS task definition dynamically

Deploys updated service with rolling updates

🔐 Secrets Management

Configured via GitHub Secrets:

AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

ECR_REPO_URL

ECS_CLUSTER_NAME

ECS_SERVICE_NAME

🏷️ Versioning & Rollback Strategy

Each deployment tagged with commit SHA

Ensures traceability and reproducibility

🔁 Rollback

Manual rollback supported via workflow input:

image_tag = <previous_commit_sha>
🩺 Application Endpoints
Endpoint	Description
/	Main application
/health	Health check
📊 Observability

Logs streamed to AWS CloudWatch

Log group: /ecs/ecsTaskExecutionRole

Enables debugging and monitoring of container behavior

🔐 Security Considerations

IAM roles used for ECS task execution

Secrets stored securely in GitHub

No hardcoded credentials in codebase

📈 Potential Enhancements

🔹 Add Application Load Balancer (ALB)

🔹 Implement HTTPS using ACM

🔹 Introduce auto-scaling policies

🔹 Add health checks at load balancer level

🔹 Integrate monitoring (Prometheus / Grafana)

🔹 Add unit & integration tests

🔹 Blue/Green deployment strategy

🧪 Local Development
python app.py

Access:

http://localhost:80
💼 Why This Project Matters

This project showcases:

Real-world DevOps workflow automation

Hands-on experience with cloud-native deployment

Understanding of container lifecycle & orchestration

Ability to design scalable and maintainable infrastructure

👨‍💻 Author

Rahul
DevOps Enthusiast | Cloud & Automation Learner
