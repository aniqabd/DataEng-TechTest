# DataEng-TechTest

This project includes an Automatic Speech Recognition (ASR) application designed to transcribe audio files. The setup involves running the ASR app locally using Docker, and a searchui application is also deployed on AWS.

## Getting Started:
These instructions will guide you through the process of setting up and running the ASR application for task 2 locally. A link is provided to access the searchui application on AWS.

## Prerequisites:
- Docker installed on your machine.
- Access to the command line or terminal.

## Clone project from repository

First, clone the project repository to your local machine:

```
git clone https://github.com/aniqabd/DataEng-TechTest.git
```

## Docker initialisation

To build the Docker Image, navigate to the directory where the Dockerfile is located and build the Docker image for the ASR application:

```
docker build -t asr-api .
```

Once the image is built, you can run the ASR application by starting a Docker container:

```
docker run -p 8001:8001 asr-api
```

This command runs the asr-app Docker container and maps port 8001 of the container to port 8001 on your host machine, allowing you to access the ASR application locally.

## Accessing the Deployed Searchui Application on AWS (Non-functional):

You can use the application by visiting the following URL:
http://54.252.173.69:3000

## Notice:
- Task 2 is functioning well with docker
- Although the AWS link is accessible, it is not a functional searchui application. This is due to connection issues with Elasticsearch which I am unable to fix.