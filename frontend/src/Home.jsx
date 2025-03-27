import React from "react";
import { useAuth } from "./context/AuthContext";
import { useNavigate } from "react-router-dom";

const Home = () => {
  const navigate = useNavigate();
  const { user, logout } = useAuth();

  const handleSignOut = async () => {
    try {
      logout();
      navigate("/login", { replace: true });
    } catch (error) {
      console.error("Logout failed:", error);
    }
  };

  if (!user) {
    navigate("/login");
    return null;
  }

  return (
    <div className="min-h-screen bg-white">
      {/* Mobile-first navigation */}
      <nav className="fixed top-0 left-0 right-0 bg-white shadow-sm z-10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex-shrink-0">
              <span className="text-gray-900 text-lg font-medium">
                Your Company Name Here
              </span>
            </div>
            <button
              onClick={handleSignOut}
              className="inline-flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-gray-700 bg-gray-50 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors duration-200"
            >
              Sign Out
            </button>
          </div>
        </div>
      </nav>

      {/* Main content */}
      <main className="pt-16 pb-8 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto">
          {/* Welcome section */}
          <div className="mt-8 sm:mt-12 text-center">
            <h1 className="text-4xl sm:text-5xl font-bold text-gray-900 tracking-tight">
              Welcome, {user.first_name}!
            </h1>
            <p className="mt-4 text-xl text-gray-600">
              We're glad to have you here
            </p>
          </div>

          {/* User info card */}
          <div className="mt-8 sm:mt-12 bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
            <div className="px-4 py-5 sm:p-6">
              <div className="space-y-4">
                <div className="flex flex-col sm:flex-row sm:items-center justify-between">
                  <div className="text-sm font-medium text-gray-500">
                    Full Name
                  </div>
                  <div className="text-base text-gray-900">
                    {user.first_name} {user.last_name}
                  </div>
                </div>
                <div className="flex flex-col sm:flex-row sm:items-center justify-between">
                  <div className="text-sm font-medium text-gray-500">Email</div>
                  <div className="text-base text-gray-900">{user.email}</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Home;
