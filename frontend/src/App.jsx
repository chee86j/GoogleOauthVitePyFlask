import React, { useState } from 'react';
import SignIn from './components/SignIn';
import Home from './Home';

function App() {
  const [user, setUser] = useState(null);
  
  const onLoginSuccess = (userData) => {
    setUser(userData);
  }

  return (
      <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
          {user ? <Home user={user} /> : <SignIn onLoginSuccess={onLoginSuccess} />}
      </div>
  );
}

export default App;