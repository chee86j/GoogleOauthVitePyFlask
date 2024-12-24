import React, { useState, useEffect } from 'react';
import axios from 'axios';

const googleButtonStyles = {
    backgroundColor: '#4285F4', // Google blue
    color: 'white',
    padding: '10px 15px',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
    fontSize: '16px',
    transition: 'background-color 0.3s ease',
};

const googleButtonHoverStyles = {
    backgroundColor: '#357ae8', // Darker Google blue
};

function SignIn({ onLoginSuccess }) {
const [buttonStyle, setButtonStyle] = useState(googleButtonStyles);
  
  const handleSignIn = () => {
    const googleUrl = 'https://accounts.google.com/o/oauth2/v2/auth';
    const scope = 'email profile';
    const responseType = 'token';
    const clientId = import.meta.env.VITE_GOOGLE_CLIENT_ID;
    const redirectUrl = 'http://localhost:5173/oauth2callback'; //Ensure correct redirect URL

    const fullUrl = `${googleUrl}?scope=${scope}&response_type=${responseType}&client_id=${clientId}&redirect_uri=${redirectUrl}`;

    window.location = fullUrl;
  };

    useEffect(() => {
        const handleCallback = async () => {
        const hash = window.location.hash;
        if(hash) {
          const accessToken = hash.substring(hash.indexOf('=') + 1, hash.indexOf('&'));
          
          try {
            const response = await axios.post('http://localhost:8000/api/login', { token: accessToken });
            if(response.status === 200) {
              onLoginSuccess(response.data);
              window.location.hash = '';
            }
          } catch (error) {
              console.error("Failed to login with Google token", error)
              window.location.hash = '';
          }
        }
        };
  
        handleCallback();
      }, [onLoginSuccess])

  const handleMouseEnter = () => {
      setButtonStyle({ ...googleButtonStyles, ...googleButtonHoverStyles });
  };

  const handleMouseLeave = () => {
      setButtonStyle(googleButtonStyles);
  };

    return (
      <div className="bg-white p-8 rounded shadow-md">
        <h2 className="text-2xl font-semibold mb-4">Sign In</h2>
        <button
          style={buttonStyle}
          onClick={handleSignIn}
          onMouseEnter={handleMouseEnter}
          onMouseLeave={handleMouseLeave}
        >
          Sign In with Google
        </button>
      </div>
    );
}

export default SignIn;