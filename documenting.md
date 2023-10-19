# API Documentation for Your Flask API

**Version:** 1.0

## Introduction

This document provides detailed information about the endpoints, request methods, and data formats for the Flask API of our application.

## Base URL

All endpoints described in this document are relative to the base URL of the API.

Base URL: `https://xander.pythonanywhere.com`

## Authentication

The API uses token-based authentication. Users must include their access token in the request headers for authentication.

- **Header**: `Authorization: Bearer {access_token}`

## Endpoints

### 1. Register User

- **Endpoint**: `/register`
- **Method**: POST
- **Description**: Register a new user (student or instructor).
- **Request Body**:
  - `user_type` (string): Type of user (student or instructor).
  - `username` (string): User's username.
  - `password` (string): User's password.
  - Other user details based on the `user_type`.
- **Response**:
  - HTTP 201 Created: User registration successful.
  - HTTP 400 Bad Request: Invalid request data.
  - HTTP 500 Internal Server Error: Registration error.

- **Example Request**:
  ```json
  POST https://xander.pythonanywhere.com/register
  {
    "user_type": "student",
    "username": "john_doe",
    "password": "secret123",
    "first_name": "John",
    "last_name": "Doe",
    "gender": "Male",
    "phone": "123-456-7890",
    "email": "john.doe@example.com",
    "telegram_id": "johndoe123",
    "faculty": "Engineering",
    "department": "Computer Science",
    "disciplinary_status": "Good Standing",
    "current_semester": 3
  }

### 2. Login User

- **Endpoint**: `/login`
- **Method**: POST
- **Description**: Authenticate a user and obtain an access token.
- **Request Body**:
  - `username` (string): User's username.
  - `password` (string): User's password.
- **Response**:
  - HTTP 200 OK: Successful login, returns an access token.
  - HTTP 401 Unauthorized: Invalid credentials.

- **Example Request**:
  ```json
  POST https://xander.pythonanywhere.com/login
  {
    "username": "john_doe",
    "password": "secret123"
  }
  ```

###  3. Logout User
**Endpoint**: `/logout`
**Method**: POST
**Description**: Invalidate the user's access token to log them out.
**Request Header**:
 - Authorization: Bearer {access_token} (Access token obtained during login)
**Response**:
 - HTTP 200 OK: Successful logout.
 - HTTP 401 Unauthorized: Access token is missing or invalid.