# FastAPI Blog Application

## Overview
This FastAPI application provides a simple backend for managing blog posts and user authentication using JSON Web Tokens (JWT). It's designed to be a lightweight and extensible solution.

## Features
- **Greeting Endpoint:** `/` - A simple endpoint to greet users.
- **Blog Endpoints:** 
  - `/blogs`: Retrieve all blog posts.
  - `/blogs/{id}`: Retrieve a specific post by ID.
  - `/blogs/` (POST): Add a new blog post (requires JWT authentication).
- **User Endpoints:** 
  - `/user/signup/` (POST): User registration.
  - `/user/signin/` (POST): User authentication (returns JWT token).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fastapi-blog-app.git
   cd fastapi-blog-app

2. Install Dependencies:
    ```bash
    pip install -r requirements.txt

## Usage
1. Run the FastAPI application:
    ```bash
    uvicorn main:app --reload

2. Access the Swagger documentation at http://127.0.0.1:8000/docs or the ReDoc documentation at http://127.0.0.1:8000/redoc for API reference and testing. 

## Configuration
- Set up your environment variables in a .env file:
    # Example
    ```bash
    SECRET_KEY=yoursecretkey

## Project Structure
- 