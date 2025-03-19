#!/bin/bash
echo "Building the application..."

# 1. Set up a Python virtual environment (if needed)
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies from requirements.txt
echo "Installing dependencies..."
pip install -r requirements.txt

# 3. Run unit and integration tests (if tests are available)
echo "Running tests..."
pytest tests/unit_tests.py  # Adjust the path if needed
pytest tests/integration_tests.py  # Adjust the path if needed

# 4. Optionally, add database migrations (if you're using Flask-Migrate)
echo "Running database migrations..."
# flask db migrate  # Uncomment if using Flask-Migrate
# flask db upgrade  # Uncomment if using Flask-Migrate

# 5. Build the Docker container (if you're containerizing the app)
echo "Building Docker container..."
docker build -t myapp .

# Completion message
echo "Build completed successfully!"

