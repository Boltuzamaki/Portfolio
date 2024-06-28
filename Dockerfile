# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install OpenSSL to create a self-signed certificate
RUN apt-get update && apt-get install -y openssl

# Create SSL certificate and key
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /home/ec2-user/portfolio/Portfolio/private.key -out /home/ec2-user/portfolio/Portfolio/certfile.crt -subj "/CN=localhost"

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches using HTTPS
CMD ["flask", "run", "--host=0.0.0.0", "--cert=/home/ec2-user/portfolio/Portfolio/certfile.crt", "--key=/home/ec2-user/portfolio/Portfolio/private.key"]
