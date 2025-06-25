#!/bin/bash

echo "Setting up Quantum Computing with Qiskit environment..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed or not in PATH. Please install Python 3.7 or higher."
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv qiskit_env
if [ $? -ne 0 ]; then
    echo "Failed to create virtual environment. Please make sure venv module is available."
    exit 1
fi

# Activate virtual environment
echo "Activating virtual environment..."
source qiskit_env/bin/activate
if [ $? -ne 0 ]; then
    echo "Failed to activate virtual environment."
    exit 1
fi

# Install requirements
echo "Installing required packages..."
pip install -r src/requirements.txt
if [ $? -ne 0 ]; then
    echo "Failed to install required packages."
    exit 1
fi

echo ""
echo "Setup completed successfully!"
echo ""
echo "To activate the environment, run: source qiskit_env/bin/activate"
echo "To run examples, use: python src/hello_quantum.py"
echo ""
