# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files to the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Run the Django application (replace with the correct management command)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
