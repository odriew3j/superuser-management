---

# 🚀 SuperUser Management System

This project is a **SuperUser Management System** built with a **Flask backend** and a **React frontend**. It allows you to create and manage super users, with data stored in a **PostgreSQL** database. The project is containerized using **Docker** and orchestrated with **Docker Compose**.

---

## 📂 Project Structure

```
superuser-management/
├── backend/                  # Flask backend
│   ├── app.py                # Flask application entry point
│   ├── config.py             # Configuration settings
│   ├── extensions.py         # Database extensions
│   ├── requirements.txt      # Python dependencies
│   ├── Dockerfile            # Dockerfile for backend
│   ├── route/                # API routes
│   ├── controller/           # Controllers for handling requests
│   ├── service/              # Business logic
│   ├── model/                # Database models
├── frontend/                 # React frontend
│   ├── src/                  # React source code
│   ├── public/               # Static assets
│   ├── package.json          # Node.js dependencies
│   ├── vite.config.js        # Vite configuration
│   ├── Dockerfile            # Dockerfile for frontend
├── docker-compose.yml.sample # Docker Compose configuration
├── nginx.conf.sample         # Nginx configuration
├── .gitignore                # Files to ignore in Git
├── README.md                 # This file
```

---

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:

- **Docker** and **Docker Compose**
- **Node.js** (for local frontend development)
- **Python** (for local backend development)
- **PostgreSQL** (optional, for local development)

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/superuser-management.git
cd superuser-management
```

### 2. Set Up Environment Variables

Create a `.env` file in the `backend` folder with the following content:

```env
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://postgres:password@localhost/postgres
```

### 3. Run with Docker Compose

Rename `docker-compose.yml.sample` to `docker-compose.yml` and `nginx.conf.sample` to `nginx.conf`. Then, start the services:

```bash
docker-compose up --build
```

This will start:
- **Backend**: Flask app on port `5000`
- **Frontend**: React app on port `5173`
- **Database**: PostgreSQL on port `5432`
- **Nginx**: Reverse proxy on port `80`

### 4. Access the Application

- **Frontend**: Open `http://localhost:5173` in your browser.
- **Backend API**: Access `http://localhost:5000/api/users`.

---

## 🖥️ Local Development

### Backend (Flask)

1. Navigate to the `backend` folder:
   ```bash
   cd backend
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

### Frontend (React)

1. Navigate to the `frontend` folder:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the React app:
   ```bash
   npm run dev
   ```

---

## 🌐 API Endpoints

| Method | Endpoint          | Description                     |
|--------|-------------------|---------------------------------|
| GET    | `/api/users`      | Get all super users             |
| POST   | `/api/users`      | Create a new super user         |

---

## 🐳 Docker Configuration

### Backend Dockerfile

```Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

### Frontend Dockerfile

```Dockerfile
FROM node:16
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "run", "dev"]
```

### Docker Compose

The `docker-compose.yml` file defines the following services:
- **backend**: Flask app
- **frontend**: React app
- **db**: PostgreSQL database
- **nginx**: Reverse proxy

---

## 🛑 Troubleshooting

### 1. Database Connection Issues
- Ensure PostgreSQL is running and the connection string in `config.py` is correct.
- Check the logs for any database errors.

### 2. Frontend Not Connecting to Backend
- Ensure the proxy configuration in `vite.config.js` points to the correct backend URL.
- Check the network tab in your browser's developer tools for errors.

### 3. Docker Issues
- Ensure Docker and Docker Compose are installed and running.
- Use `docker-compose logs` to check the logs for errors.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Flask**: For the backend framework.
- **React**: For the frontend library.
- **PostgreSQL**: For the database.
- **Docker**: For containerization.

---

Enjoy building and managing super users! 🎉
