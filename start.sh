#!/bin/bash

# Create a directory for the model
mkdir -p models

# Download the model from GitHub Releases
wget -O Models/t5_grammar_correction/model.safetensors "https://github.com/vivek-c29/Grammar-Correcter/releases/download/v1.0/model.safetensors"

# Start the application
pip install sentencepiece
python app.py
