import React from 'react';

const Home = () => {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-r from-blue-500 to-purple-600 text-white">
      <header className="text-center mb-8">
        <h2 className="text-2xl font-semibold mb-4">Welcome {user.first_name} {user.last_name} to the App!</h2>
        <p className="text-lg font-light">
          We’re thrilled to have you here. Explore the features, connect with others, and make the most out of our services.
        </p>
      </header>
      
      <div className="mt-6">
        <img 
          src="/welcome-image.png" 
          alt="Welcome illustration" 
          className="max-w-md mx-auto rounded-lg shadow-lg"
        />
      </div>
      
      <div className="mt-10">
        <button className="px-6 py-3 bg-green-500 hover:bg-green-600 text-white rounded-lg shadow-md transition-transform transform hover:scale-105">
          Get Started
        </button>
      </div>

      <footer className="absolute bottom-5 text-center text-sm">
        <p>&copy; {new Date().getFullYear()} Our Platform. All Rights Reserved.</p>
        <p>Have questions? <a href="/contact" className="text-yellow-300 underline">Contact us</a>.</p>
      </footer>
    </div>
  );
};

export default Home;
