
# 🚀 Event Announcement System using AWS SNS, Lambda, API Gateway, and S3

I built a **fully serverless Event Announcement System** using AWS services like **SNS**, **Lambda**, **API Gateway**, and **S3**, aimed at automating and scaling event notifications through email.

This project demonstrates modern cloud architecture and integrates multiple AWS services to create a responsive, secure, and scalable backend.

---

## 🌐 Live Demo Flow

1. **Frontend** hosted on Amazon S3 as a static website.
2. **User submits** an event announcement via the form.
3. **API Gateway** receives the request and triggers a Lambda function.
4. **Lambda** publishes the event message to an **SNS topic**.
5. **SNS** notifies all **subscribed email recipients** instantly.

---

## 🔧 Technologies Used

- **Amazon S3** – Hosts the frontend HTML form.
- **Amazon API Gateway** – Manages RESTful endpoints.
- **AWS Lambda** – Handles business logic (Node.js).
- **Amazon SNS** – Sends real-time email notifications.
- **IAM Roles & Policies** – For secure communication between services.

---

## 🖼️ Architecture Diagram

![System Architecture ](https://github.com/user-attachments/assets/ce25a7e6-63ca-41f9-bd8c-f85cb9665cf0)



---

## ✅ Features

- Serverless deployment
- Real-time email alerts
- Scalable and cost-effective
- Easy to extend with additional logic (e.g., logging, DynamoDB)

---

## 📌 What I Learned

- Designing event-driven serverless architectures
- Integrating multiple AWS services in real-world use cases
- Using API Gateway with Lambda securely
- Configuring and subscribing to SNS topics for notifications
- Hosting and connecting a static site via S3 and API Gateway

---




