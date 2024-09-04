# Contact List Management App

## Overview

This project is a full-stack web application for managing a contact list with Create, Read, Update, and Delete (CRUD) operations. The frontend is built using React, which interacts with a REST API powered by Flask on the backend. The app allows users to view a list of contacts, create new contacts, update existing ones, and delete contacts.

## Features

- **View Contacts**: Displays a list of contacts with details such as first name, last name, and email.
- **Create Contact**: Allows users to create a new contact via a pop-up form.
- **Update Contact**: Users can update existing contacts by clicking an "Update" button.
- **Delete Contact**: Users can delete a contact, which will be removed from the list.

## Technologies Used

### Frontend

- **React**: JavaScript library for building user interfaces.
- **CSS/SCSS**: For styling the components.
- **Fetch API**: Used for making HTTP requests to the Flask backend.

### Backend

- **Flask**: Python web framework for building the REST API.
- **SQLite**: Database used for storing contacts (can be replaced with another database system).

## Setup and Installation

### Prerequisites

- **Python 3.x** installed on your machine.
- **Node.js** and **npm** installed for the React frontend.
- **SQLite** (or another database system if configured differently).

### Backend Setup (Flask)

1. Navigate to the `backend` directory:

   ```bash
   cd backend
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```bash
   flask run
   ```
   The backend server will start running on `http://127.0.0.1:5000/`.

### Frontend Setup (React)

1. Navigate to the `frontend` directory:

   ```bash
   cd frontend
   ```

2. Install Node.js dependencies:

   ```bash
   npm install
   ```

3. Start the React application:
   ```bash
   npm start
   ```

## Usage

- **View Contacts**: Open the application in your browser. The contact list will be displayed.
- **Create Contact**: Click the "Create New Contact" button, fill in the form, and submit to add a new contact to the list.
- **Update Contact**: Click the "Update" button next to a contact, modify the details, and submit the form to update the contact's information.
- **Delete Contact**: Click the "Delete" button next to a contact to remove it from the list.

## API Endpoints

The following endpoints are provided by the Flask REST API:

- **GET `/contacts`**: Retrieves the list of contacts.
- **POST `/create_contact`**: Creates a new contact.
- **PATCH `/update_contact/<int:user_id>`**: Updates an existing contact by its ID.
- **DELETE `/delete_contact/<int:user_id>`**: Deletes a contact by its ID.

## License

This project is open-source and available under the [MIT License](LICENSE).
