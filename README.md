# LinkHub
# LinkHub Project

A simple, containerized web application built with Python and Flask. This project serves as a personal learning exercise.

## Purpose

The primary goal of this project is educational. It is a practical exercise for the following purposes:

* Re-learning the fundamentals of the Python programming language.
* Learning core DevOps and back-end development concepts, including:
    * Containerization with Docker.
    * Multi-service application management with Docker Compose.
    * Basic web application development with the Flask framework.

**Note:** This application is a learning tool and is not intended for any practical or production use.

## Technologies Used

* **Language:** Python 3.10
* **Framework:** Flask
* **Database:** PostgreSQL
* **Containerization:** Docker, Docker Compose

## How to Run

1.  Ensure you have Docker and Docker Compose installed.
2.  Create a `.env` file in the project root with the required database credentials (`POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`).
3.  From the project's root directory, run the following command:

    sudo docker-compose up --build

4.  The application will be available at `http://localhost:8080`.
