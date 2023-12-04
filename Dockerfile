# Use an official Python runtime as a parent image
FROM continuumio/miniconda3

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Update the Conda environment
RUN conda update -n base -c defaults conda

# Create the Conda environment
RUN conda env create -f environment.yml

# Make RUN commands use the new environment
SHELL ["conda", "run", "-n", "network_analysis_env", "/bin/bash", "-c"]

# Install the spaCy model
RUN python -m spacy download en_core_web_sm

# Make sure the environment is activated:
RUN echo "Make sure flask is installed:"
RUN python -c "import flask"

# Define the command to run your application or tests
CMD ["python", "view_tree.py"]