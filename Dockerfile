# 1. Use an official Python runtime as a parent image
FROM python:3.11-slim-bullseye

# 2. Set the working directory in the container
WORKDIR /app

# 3. Copy the requirements file into the container
COPY requirements.txt .

# 4. Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application's code into the container
COPY . .

# 6. Expose the port the app runs on
# The default Gunicorn port is 8000
EXPOSE 8000

# 7. Define the command to run the application
# This command tells Gunicorn to run the app created by the `create_app` factory.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:create_app()"]
