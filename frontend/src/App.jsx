import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Routes, Route, Navigate } from 'react-router-dom';
import SignIn from './components/SignIn';
import Home from './Home';

function App() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const checkAuthStatus = async () => {
      try {
        const response = await axios.get(
          `${import.meta.env.VITE_API_BASE_URL}/api/check-auth`, 
          { withCredentials: true }
        );
        if (response.status === 200) {
          const userData = response.data;
          setUser(typeof userData === 'string' ? JSON.parse(userData) : userData);
        }
      } catch (error) {
        if (error.response?.status !== 401) {
          console.error('Authentication error:', error);
        }
        setUser(null);
      } finally {
        setLoading(false);
      }
    };

    checkAuthStatus();
  }, []);

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-gray-100">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-gray-900"></div>
      </div>
    );
  }

  return (
    <Routes>
      <Route 
        path="/signin" 
        element={user ? <Navigate to="/" /> : <SignIn onLoginSuccess={setUser} />} 
      />
      <Route 
        path="/" 
        element={
          user ? (
            <Home user={user} setUser={setUser} />
          ) : (
            <Navigate to="/signin" replace />
          )
        } 
      />
    </Routes>
  );
}

export default App;