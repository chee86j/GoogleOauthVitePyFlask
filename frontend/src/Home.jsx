import React from 'react';

function Home({ user }) {
    return (
        <div className="bg-white p-8 rounded shadow-md">
            <h2 className="text-2xl font-semibold mb-4">Welcome {user.first_name} {user.last_name} to the App!</h2>
        </div>
    );
}

export default Home;