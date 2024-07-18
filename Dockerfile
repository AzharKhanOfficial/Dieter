# Use an appropriate Python base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Install pip dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose any necessary ports
EXPOSE 8000

# Define the command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
