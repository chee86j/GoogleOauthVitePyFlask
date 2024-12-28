import React from 'react';
import PropTypes from 'prop-types';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const Home = ({ user, setUser }) => {
  const navigate = useNavigate();

  const handleSignOut = async () => {
    try {
      await axios.post(
        `${import.meta.env.VITE_API_BASE_URL}/api/logout`,
        {},
        { withCredentials: true }
      );
      
      // Clear the user state in App.jsx
      setUser(null);
      
      // Force navigation to signin
      navigate('/signin', { replace: true });
    } catch (error) {
      console.error('Logout failed:', error);
      alert('Failed to log out. Please try again.');
    }
  };

  if (!user) {
    navigate('/signin');
    return null;
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-r from-blue-500 to-purple-600 text-white">
      <div className="absolute top-4 right-4">
        <button
          onClick={handleSignOut}
          className="px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded-md shadow-md transition-colors"
        >
          Sign Out
        </button>
      </div>
      
      <header className="text-center mb-8">
        <h2 className="text-2xl font-semibold mb-4">
          Welcome {user.first_name} {user.last_name}!
        </h2>
        <p className="text-lg font-light">
          You're signed in with {user.email}
        </p>
      </header>
    </div>
  );
};

Home.propTypes = {
  user: PropTypes.shape({
    first_name: PropTypes.string,
    last_name: PropTypes.string,
    email: PropTypes.string
  }),
  setUser: PropTypes.func.isRequired
};

export default Home;
