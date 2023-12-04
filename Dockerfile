# Use an official Python runtime as a base image
FROM python:3.10.12

# Seting the working directory
WORKDIR /app

# Copy the entire project directory into the container
COPY . /app

# Install necessary dependencies using pip
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt

# Define the command to run your application or tests
CMD ["/opt/conda/bin/python", "view_tree.py"]
