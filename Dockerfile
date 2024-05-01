# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Make port 8000 available to the world outside this container
EXPOSE 8000

# Collect static files
RUN python manage.py collectstatic --noinput

# Run app.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
