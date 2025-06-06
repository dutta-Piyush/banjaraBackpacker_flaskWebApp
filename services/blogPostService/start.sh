#!/bin/bash

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL to be ready..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL is ready!"

# Run database initialization
cd /app
python -c "import sys; sys.path.append('/app'); from app.utils.db_creation import app; print('Database tables created for blog service')"

# Start the Flask application
python run.py 