# FastAPI Project with PostgreSQL and JWT Authentication

This project demonstrates a FastAPI application with JWT-based user authentication and PostgreSQL as the database. The application interacts with the CoinGecko API to retrieve cryptocurrency market data.

## Features
- User authentication with JWT tokens.
- User login and token generation.
- CRUD operations with PostgreSQL.
- Interacts with the CoinGecko API for cryptocurrency data.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- [Python 3.7+](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Pip](https://pip.pypa.io/en/stable/installation/)

## Setting Up the Environment

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   
2. **Create a .env file in the project directory to store environment variables. Below is a template**:
   ```bash
   # Encryption key for JWT
 SECRET_KEY=your_secret_key_here
 
 # PostgreSQL database credentials
 DB_NAME=crypto
 DB_PASSWORD=your_database_password_here
 DB_HOST=localhost
 DB_PORT=5432
 
 # JWT Expiration Time
 JWT_EXPIRATION_TIME=30

Replace your_secret_key_here and your_database_password_here with your own values.

Create a virtual environment and activate it:

For Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```
For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install the dependencies:**
```bash
pip install -r requirements.txt
```

Set up PostgreSQL:

Make sure PostgreSQL is installed and running.

**Create the database specified in your .env file. You can do this by connecting to PostgreSQL and running the following commands**:

```bash
CREATE DATABASE crypto;
CREATE USER your_user WITH PASSWORD 'your_password';
ALTER ROLE your_user SET client_encoding TO 'utf8';
ALTER ROLE your_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE your_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE crypto TO your_user;
```

**Apply the migrations**:

Ensure that your database is set up properly by running the migration commands:
```
alembic upgrade head
```

**Running the Application**
Once the setup is complete, you can run the FastAPI application using uvicorn.

Run the FastAPI app:

```
uvicorn main:app --reload
```
The application will run at http://127.0.0.1:8000. You can open this in your browser to access the API.

3. **Authentication and Authorization**:

**Signup: send a POST request to http://127.0.0.1:8000/auth/signup with the following JSON payload:**

```
{
"name": "your_name",
  "username": "your_username",
  "password": "your_password"
}
```

**Login: To obtain a JWT token, send a POST request to to http://127.0.0.1:8000/auth/signup with the following JSON payload:**

```
{
  "username": "your_username",
  "password": "your_password"
}
```
**Protected Routes: Once authenticated, use the Authorization header with the Bearer token in requests to access protected routes, e.g.,:**

Authorization: Bearer <your_jwt_token>

**Now you can make the following get requests with the JWT token**:
1. List all coins including coin id.
2. List coin categories
3. List specific coins according to id from listing endpoint and/or category from categories
endpoint. Listing should show market data against the Canadian Dollar.

```
http://0.0.0.0:8000/coins/?page_num=2&per_page=10
http://0.0.0.0:8000/categories
http://0.0.0.0:8000/coins/hedera-hashgraph
```

