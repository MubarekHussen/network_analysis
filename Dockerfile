# Use an official Python runtime as a base image
FROM python:3.10.12

# Seting the working directory
WORKDIR /app

# Copy the entire project directory into the container
COPY . /app

# Install necessary dependencies using conda
RUN apt-get update && apt-get install -y wget && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda && \
    rm Miniconda3-latest-Linux-x86_64.sh && \
    /opt/conda/bin/conda install -c conda-forge --yes --file requirements.txt && \
    /opt/conda/bin/conda clean -afy && \
    /opt/conda/bin/python -m pip install --upgrade pip

# Define the command to run your application or tests
CMD ["/opt/conda/bin/python", "view_tree.py"]
