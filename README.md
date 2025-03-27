# GoogleOauthVitePyFlask

A modern full-stack web application demonstrating Google OAuth 2.0 integration using React (Vite) and Flask. This project showcases secure user authentication, protected routes, and a clean, modern UI built with Tailwind CSS.

## Project Structure

```
├── backend/
│   ├── __init__.py          # Flask app initialization
│   ├── app.py               # Main application entry point
│   ├── config.py            # Configuration settings
│   ├── extensions.py        # Flask extensions initialization
│   ├── google_oauth.py      # Google OAuth implementation
│   ├── models.py            # Database models
│   ├── routes.py            # API endpoints
│   ├── seed.py             # Database seeding script
│   └── requirements.txt     # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── context/       # React context providers
│   │   ├── App.jsx        # Main React component
│   │   ├── Home.jsx       # Home page component
│   │   └── main.jsx       # React entry point
│   ├── package.json       # JavaScript dependencies
│   └── tailwind.config.js # Tailwind CSS configuration
└── .env                   # Environment variables
```

## Tech Stack

### Backend (Flask)
- **Flask 3.0.2**: Modern Python web framework
- **Flask-SQLAlchemy 3.1.1**: SQL ORM for Python
- **Flask-Migrate 4.0.7**: Database migration handling
- **Flask-JWT-Extended 4.6.0**: JWT authentication
- **Flask-CORS 4.0.0**: Cross-Origin Resource Sharing
- **PostgreSQL**: Database (via psycopg2-binary 2.9.9)

### Frontend (React + Vite)
- **React 18.2.0**: UI library
- **Vite 5.1.6**: Build tool and dev server
- **@react-oauth/google 0.12.1**: Google OAuth integration
- **React Router 6.22.3**: Client-side routing
- **Tailwind CSS 3.4.1**: Utility-first CSS framework

## Getting Started

### Prerequisites
- Python 3.x
- Node.js and npm
- PostgreSQL database
- Google Cloud Console account

### Backend Setup

1. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   Create `.env` in the backend directory with:
   ```
   FLASK_APP=app.py
   FLASK_ENV=development
   DATABASE_URL=postgresql://username:password@localhost/dbname
   GOOGLE_CLIENT_ID=your_client_id
   GOOGLE_CLIENT_SECRET=your_client_secret
   JWT_SECRET_KEY=your_jwt_secret
   ```

4. Initialize database:
   ```bash
   flask db upgrade
   python seed.py  # Optional: seed initial data
   ```

5. Run the server:
   ```bash
   flask run
   ```

### Frontend Setup

1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Configure environment variables:
   Create `.env` in the frontend directory with:
   ```
   VITE_API_BASE_URL=http://localhost:5000
   ```

3. Start development server:
   ```bash
   npm run dev
   ```

## Google OAuth Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project or select existing one
3. Enable Google Identity Services API
4. Configure OAuth 2.0 credentials:
   - Authorized JavaScript origins:
     ```
     http://localhost:5173
     ```
   - Authorized redirect URIs:
     ```
     http://localhost:5000/login/google/authorized
     ```
5. Copy Client ID and Client Secret to your `.env` files

## Development

- Backend API runs on `http://localhost:5000`
- Frontend dev server runs on `http://localhost:5173`
- API endpoints are CORS-enabled for frontend origin
- JWT tokens are used for session management

## Security Notes

- Store sensitive data in `.env` files (never commit to version control)
- Use HTTPS in production
- Keep Google OAuth credentials secure
- Implement proper error handling and validation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is open source and available under the MIT License.