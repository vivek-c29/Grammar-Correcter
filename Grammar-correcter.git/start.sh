#!/bin/bash

# Create a directory for the model
mkdir -p models

# Download the model from GitHub Releases
wget -O models/model.safetensors "https://github.com/vivek-c29/Grammar-correcter/releases/download/v1.0/model.safetensors"

# Start the application
python app.py
