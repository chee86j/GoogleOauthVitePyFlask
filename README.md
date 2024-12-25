# GoogleOauthVitePyFlask

A full-stack web application integrating Google OAuth 2.0 for user authentication. 
The project uses a **Vite-powered React frontend** and a **Flask backend**.

## Features

- **Google OAuth 2.0 Authentication**: Secure user login with Google.
- **Frontend**: Built with React and Vite for fast and modular development.
- **Backend**: Python Flask with SQLAlchemy for managing user data.
- **RESTful API**: Provides endpoints for user authentication and data handling.
- **CORS Enabled**: Ensures communication between the frontend and backend is secure.
- **Environment Configuration**: Manages sensitive credentials using `.env` files.

---

## Backend Setup

1. **Create a Python Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r backend/requirements.txt
   ```

3. **Set up the Database**
   - Update the `.env` file with your PostgreSQL credentials.
   - Initialize the database:
     ```bash
     flask db init
     flask db migrate
     flask db upgrade
     ```

4. **Run the Flask Server**
   ```bash
   python backend/app.py
   ```

---

## Frontend Setup

1. **Navigate to the Frontend Directory**
   ```bash
   cd frontend
   ```

2. **Install Dependencies**
   ```bash
   npm install
   ```

3. **Start the Development Server**
   ```bash
   npm run dev
   ```

---

## Environment Variables

Create a `.env` file in the root directory with the following keys:

```plaintext
# Backend
DB_USERNAME=your_db_username
DB_PASSWORD=your_db_password
DB_NAME=your_db_name
JWT_SECRET_KEY=your_jwt_secret_key

# Google OAuth
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GOOGLE_REDIRECT_URI=http://localhost:5173/api/auth/callback

# Frontend
VITE_API_BASE_URL=http://localhost:5000
```

---

## Setting Up Google OAuth 2.0

To enable Google OAuth 2.0 in your application, follow these steps:

1.  Create a Project in Google Cloud Console:
        Visit Google Cloud Console at `https://console.cloud.google.com/welcome?inv=1&invt=AblGKA&project=prop-pilot-416817`.
        Log in with your Google account.
        Click on Select a Project at the top and create a new project (or select an existing one).

2.  Enable the OAuth 2.0 API:
        Navigate to APIs & Services > Library.
        Search for and enable the "Google+ API" or "Identity Toolkit API" (depending on your specific needs).

3.  Create OAuth 2.0 Credentials:
        Go to APIs & Services > Credentials.
        Click Create Credentials and select OAuth 2.0 Client ID.
        Select the `External` application type and click Create.

        Configure the OAuth Consent Screen:
            Enter your app's name and other required details.
            Add a test user (your email or other authorized emails for testing).

        Configure the Web Application Settings:

            Choose Web Application as the application type.
            Set the following:
                Authorized JavaScript Origins:
                    `http://localhost:5173`
                Authorized Redirect URIs:
                    `http://localhost:5173/api/auth/callback`

    Save the credentials and note down your Client ID and Client Secret.