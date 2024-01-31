# Car Management API Documentation

## Introduction

The Car Management API is a simple web service built using Flask, a Python web framework. This API allows users to manage information about cars, including retrieving details of all cars, getting information about a specific car, adding a new car, and deleting a car.

## API Endpoints

### 1. Get All Cars

**Endpoint:**
GET /cars


**Description:**
Get details of all cars currently stored in the system.

**Response:**
- HTTP Status Code: 200 OK
- Body: JSON object containing information about all cars.

### 2. Get Car Details

**Endpoint:**
GET /cars/<car_id>


**Parameters:**
- `<car_id>`: The unique identifier for a specific car.

**Description:**
Get details of a specific car based on its ID.

**Response:**
- HTTP Status Code: 200 OK
- Body: JSON object containing information about the specified car.
- HTTP Status Code: 404 Not Found
- Body: JSON object with an error message if the specified car ID is not found.

### 3. Add a New Car

**Endpoint:**
POST /cars


**Body:**
JSON object containing details of the new car (name, year, price).

**Description:**
Add a new car to the system.

**Response:**
- HTTP Status Code: 200 OK
- Body: JSON object with a success message and the ID of the newly added car.

### 4. Delete a Car

**Endpoint:**
DELETE /cars/<car_id>


**Parameters:**
- `<car_id>`: The unique identifier for the car to be deleted.

**Description:**
Delete a specific car from the system.

**Response:**
- HTTP Status Code: 200 OK
- Body: JSON object with a success message if the car is deleted.
- HTTP Status Code: 404 Not Found
- Body: JSON object with an error message if the specified car ID is not found.

## File Storage

The API uses a JSON file named cars.json to store information about cars persistently. The file is created in the same directory as the script. Each car is assigned a unique ID, and its details are stored in the file.

