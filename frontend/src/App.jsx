import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
    const [users, setUsers] = useState([]);
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');

    // Fetch users from Flask backend
    useEffect(() => {
        axios.get('/api/users')
            .then((response) => setUsers(response.data))
            .catch((error) => console.error('Error fetching users:', error));
    }, []);

    // Handle form submission to create a new user
    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('/api/users', { username, email })
            .then((response) => {
                alert(`User created with ID: ${response.data.id}`);
                setUsername('');
                setEmail('');
                // Refresh the user list
                axios.get('/api/users')
                    .then((response) => setUsers(response.data))
                    .catch((error) => console.error('Error fetching users:', error));
            })
            .catch((error) => console.error('Error creating user:', error));
    };

    return (
        <div>
            <h1>Users</h1>
            <ul>
                {users.map((user) => (
                    <li key={user.id}>
                        {user.username} - {user.email}
                    </li>
                ))}
            </ul>

            <h2>Create User</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required
                />
                <input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                />
                <button type="submit">Create</button>
            </form>
        </div>
    );
}

export default App;