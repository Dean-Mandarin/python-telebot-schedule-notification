# Use the official Python image as a base image
FROM python:3.8

# Set the working directory
WORKDIR /app

# Set the timezone to Asia/Almaty
RUN ln -sf /usr/share/zoneinfo/Asia/Almaty /etc/localtime
# Copy the Python script into the container
COPY main.py .

# Install the required dependencies
RUN pip install pyTelegramBotAPI schedule

# Command to run your Python script
CMD ["python3", "main.py"]
