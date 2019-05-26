# Use an official Python runtime as a parent image
FROM python:2.7-slim
WORKDIR /app
COPY . /app

RUN pip install pystrich

RUN pip install --trusted-host pypi.python.org -r requirements.txt
# Make port 80 available to the world outside this container

EXPOSE 80

# Run app.py when the container launches
CMD ["python", "consumerfinal.py"]
