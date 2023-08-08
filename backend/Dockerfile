# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend files to the container
COPY backend /app

# Set the environment variable to point to the SQLite database file
ENV DB_PATH=db/data/todo.db

# Expose port 5000 to make the backend accessible
EXPOSE 5000

# Start the backend server
CMD ["python", "App.py"]
