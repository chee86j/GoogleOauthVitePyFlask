
# GoogleOauthVitePyFlask

A full-stack web application integrating Google OAuth 2.0 for user authentication. The project uses a **Vite-powered React frontend** and a **Flask backend**.

---

## Features

- Secure Google OAuth 2.0 authentication.
- Protected routes and session management.
- PostgreSQL database integration.
- React frontend styled with Tailwind CSS.

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

## Google OAuth 2.0 Setup

To enable Google OAuth 2.0 in your application:

1. **Create a Project in Google Cloud Console**:
   - Visit [Google Cloud Console](https://console.cloud.google.com).
   - Log in and create a new project or select an existing one.

2. **Enable the Google Identity Services API**:
   - Navigate to **APIs & Services > Library**.
   - Search for and enable the **Google Identity Services API**.

3. **Configure OAuth 2.0 Credentials**:
   - Go to **APIs & Services > Credentials**.
   - Click **Create Credentials** and select **OAuth 2.0 Client ID**.
   - Choose **External** as the application type.
   - Configure the following:
     - **Authorized JavaScript Origins**:
       ```
       http://localhost:5173
       http://127.0.0.1:5173
       ```
     - **Authorized Redirect URIs**:
       ```
       http://localhost:5000/login/google/authorized
       http://127.0.0.1:5000/login/google/authorized
       ```

4. **Save Credentials**:
   - Note the **Client ID** and **Client Secret**. Update your `.env` files as shown below.

---

## Environment Variables

### Root `.env`:
```plaintext
DB_USERNAME=postgres
DB_PASSWORD=your_password
DB_NAME=google_oauth_app_db
JWT_SECRET_KEY=your_secret_key
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GOOGLE_REDIRECT_URI=http://localhost:5000/login/google/authorized
FRONTEND_URL=http://localhost:5173
```

### Frontend `.env`:
```plaintext
VITE_API_BASE_URL=http://localhost:5000
```

---

## Tech Stack

### Backend:
- **Flask**: Backend framework for Python.
- **Flask-Dance**: Simplifies OAuth integrations.
- **Flask-SQLAlchemy**: ORM for managing database interactions.
- **PostgreSQL**: Database for storing user and session data.
- **Flask-Migrate**: Handles database migrations.
- **Flask-Login**: Provides session management.

### Frontend:
- **React**: For building interactive user interfaces.
- **React Router**: Enables client-side routing.
- **Axios**: Handles API requests between the frontend and backend.
- **Tailwind CSS**: Provides utility-first CSS for styling.
- **Vite**: Development server and build tool for fast frontend development.

---

## Common Issues

1. **InsecureTransportError**
   - Expected in development when running on HTTP.
   - Use HTTPS in production.

2. **Database Connection**
   - Ensure PostgreSQL is running.
   - Verify database credentials in `.env`.
   - Confirm the database exists.

3. **OAuth Errors**
   - Check Google Cloud Console credentials.
   - Verify redirect URIs.
   - Ensure `.env` variables are correctly configured.

---

## Development Details

- **Backend**: Runs on `http://localhost:5000`.
- **Frontend**: Runs on `http://localhost:5173`.
- **CORS**: Configured to allow requests from the frontend origin.
- **Database Migrations**: Managed using Flask-Migrate.

---

## Security Notes

- Use HTTPS in production for secure communication.
- Never commit `.env` files to source control.
- Keep Google Client ID and Client Secret private.
