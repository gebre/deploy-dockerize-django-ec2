# Deploy Dockerized Django app on AWS Ec2  with Docker Compose, Redis, Celery, ElasticSearch, PostgreSQL Using Github Actions CI/CD Pipeline
[![LinkedIn](https://img.shields.io/badge/Connect%20with%20me%20on-LinkedIn-blue.svg)](https://www.linkedin.com/in/muhammad-rashid-daha/)
[![Youtube](https://img.shields.io/youtube/channel/subscribers/UC1HEefoqUWmztGZ_Laq28sw)](https://youtube.com/@codewithmuh)
[![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@codewithmuh)
[![GitHub](https://img.shields.io/github/stars/codewithmuh.svg?style=social)](https://github.com/codewithmuh)
[![Terraform](https://img.shields.io/badge/Terraform-%E2%9C%A8-lightgrey)](https://www.terraform.io)
[![AWS](https://img.shields.io/badge/AWS-%F0%9F%9B%A1-orange)](https://aws.amazon.com)


### Youtube Video Url: https://youtu.be/BlVR6hzZ6T0
### Linkedin Article: https://www.linkedin.com/pulse/automate-your-django-deployment-github-actions-docker-muhammad-rashid-9gfif


![DEPLOY REACT ON S3 (9)](https://github.com/user-attachments/assets/7de04635-87d2-4615-8f91-fa529b45a998)


This guide walks you through deploying a Dockerized Django backend on an AWS EC2 instance, setting up Nginx for reverse proxy, and automating deployment using GitHub Actions.

## Table of Contents

1. [Prepare your Project Locally for Production Ready](#prepare-your-project-locally-for-production-ready)
2. [AWS EC2 Instance Creation](#aws-ec2-instance-creation)
3. [Install Necessary Packages on EC2](#install-necessary-packages-on-ec2)
4. [Clone your Project on EC2](#clone-your-project-on-ec2)
5. [Nginx Setup](#nginx-setup)
6. [CI/CD Pipeline Setup with GitHub Actions: Automate Deployment](#cicd-pipeline-setup-with-github-actions-automate-deployment)
7. [Conclusion](#conclusion)


Commands:

docker compose -f "./build-process/docker-compose-django-backend.yml" up -d --build

sudo docker-compose -f "./build-process/docker-compose-django-backend.yml" up -d --build

## License
This project is licensed under MIT License, granting you the freedom to use, modify, and distribute the code.

## Acknowledgements
Special thanks to codewithmuh for creating this incredible Django Starter Kit and simplifying the development process.

## Support
<a href="https://www.buymeacoffee.com/codewithmuh" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-yellow.png" alt="Buy Me A Coffee" height="41" width="174"></a>
