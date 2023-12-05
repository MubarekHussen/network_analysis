# Use an official Python runtime as a parent image
FROM continuumio/miniconda3

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Update the system and install libpq-dev
RUN apt-get update && apt-get install -y libpq-dev

# Update the Conda environment
RUN conda update -n base -c defaults conda

# Create the Conda environment
COPY environment.yml .
RUN conda env create -f environment.yml

# Activate the Conda environment
SHELL ["conda", "run", "-n", "network_analysis_env", "/bin/bash", "-c"]

# Define the command to download spaCy model (en_core_web_sm) within the Conda environment
RUN python -m spacy download en_core_web_sm

# Make sure the environment is activated:
RUN echo "Make sure flask is installed:"
RUN python -c "import flask"

# Define the command to run your application or tests
CMD ["python", "view_tree.py"]
