# Use a base image that includes Conda
FROM continuumio/miniconda3

# Set the working directory
WORKDIR /app

# Copy the entire project directory into the container
COPY . /app

# Create the Conda environment
RUN conda env create -f environment.yml

# Activate the Conda environment and install dependencies
SHELL ["conda", "run", "-n", "network_analysis_env", "/bin/bash", "-c"]
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt

# Define the command to run your application or tests
CMD ["python", "view_tree.py"]