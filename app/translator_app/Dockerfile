# Use a slim Python image for efficiency
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dummy script into the container
COPY hello_world.py .

# Standard execution command
# Tapis will append the appArgs defined in the JSON to this command
ENTRYPOINT ["python", "hello_world.py"]