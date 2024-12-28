import React from 'react';
import PropTypes from 'prop-types';

const Home = ({ user }) => {
  if (!user) {
    return null;
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-r from-blue-500 to-purple-600 text-white">
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
  })
};

export default Home;
