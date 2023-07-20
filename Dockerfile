# Use Ubuntu as the base image
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY . /app

# Update package lists and install necessary dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip



# Install Python dependencies
RUN pip3 install -r requirements.txt


# Expose the desired port
EXPOSE 8080

# Set the entrypoint command
CMD ["python3", "app.py"]
