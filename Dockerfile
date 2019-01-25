# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /mise/mise/ticketproducer

# Copy the current directory contents into the container at /app
COPY . /ticketproducer

# Install any needed packages specified in requirements.txt


# Make port 80 available to the world outside this container
EXPOSE 9092

# Define environment variable


# Run app.py when the container launches
CMD ["python", "ticketproducer.py"]
