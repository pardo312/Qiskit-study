# Quantum Computing with Qiskit

This repository contains a collection of quantum computing examples and applications implemented using IBM's Qiskit framework. The project demonstrates various quantum computing concepts from basic principles to advanced algorithms.

## Overview

Quantum computing is a rapidly evolving field that leverages the principles of quantum mechanics to perform computations. This project provides practical examples of quantum algorithms and applications using Qiskit, IBM's open-source quantum computing framework.

## Project Structure

This project is organized into the following directories:

- **src/**: Contains all source code and example files
- **setup/**: Contains setup scripts for easy environment configuration

### Source Files

- **src/hello_quantum.py**: Introduction to quantum computing basics
  - Creates a simple quantum circuit with a Hadamard gate
  - Demonstrates quantum superposition
  - Visualizes qubit states on the Bloch sphere

- **src/advanced_quantum.py**: Advanced quantum computing concepts
  - Multi-qubit circuits
  - Quantum entanglement with CNOT gates
  - Phase manipulation with S and T gates
  - Quantum interference
  - Bell state creation
  - Advanced state visualization

- **src/grovers_algorithm.py**: Implementation of Grover's search algorithm
  - Demonstrates quantum search with quadratic speedup
  - Creates superposition of all possible states
  - Applies an oracle to mark the target state
  - Uses amplitude amplification to increase probability of the target state
  - Visualizes the results

- **src/quantum_sudoku.py**: Quantum approach to solving Sudoku puzzles
  - Uses quantum computing principles to solve 4x4 Sudoku puzzles
  - Demonstrates the Quantum Approximate Optimization Algorithm (QAOA)
  - Combines quantum and classical techniques for constraint satisfaction problems

## Visualizations

The scripts generate various visualizations to help understand quantum states and measurement results:

- **src/bloch_sphere.png**: Visualization of a single qubit state on the Bloch sphere
- **src/bloch_multivector.png**: Visualization of multi-qubit states
- **src/measurement_histogram.png**: Histogram of quantum measurement results
- **src/state_visualization.png**: Visualization of the quantum state vector
- **src/grovers_results.png**: Results of running Grover's algorithm

## Prerequisites

To run these examples, you'll need:

1. Python 3.7 or higher
2. Qiskit and related packages

## Installation

### Automated Setup (Recommended)

This repository includes setup scripts that automate the installation process:

1. Clone this repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Run the appropriate setup script for your operating system:

   **Windows:**
   ```
   setup/setup.bat
   ```

   **Linux/macOS:**
   ```
   chmod +x setup/setup.sh
   ./setup/setup.sh
   ```

   The setup script will:
   - Create a Python virtual environment (`qiskit_env`)
   - Activate the virtual environment
   - Install all required packages from `requirements.txt`

3. After setup, activate the environment:

   **Windows:**
   ```
   qiskit_env\Scripts\activate
   ```

   **Linux/macOS:**
   ```
   source qiskit_env/bin/activate
   ```

### Manual Setup

If you prefer to set up manually:

1. Clone this repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Set up a Python virtual environment (recommended):
   ```
   python -m venv qiskit_env
   source qiskit_env/bin/activate  # On Windows: qiskit_env\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r src/requirements.txt
   ```

## Usage

Run any of the example scripts using Python:

```
python src/hello_quantum.py
python src/advanced_quantum.py
python src/grovers_algorithm.py
python src/quantum_sudoku.py
```

Each script will:
1. Create and execute quantum circuits
2. Display the results
3. Generate visualizations
4. Provide explanations of the quantum concepts demonstrated

## Learning Resources

If you're new to quantum computing and Qiskit, here are some helpful resources:

- [Qiskit Documentation](https://qiskit.org/documentation/)
- [Qiskit Textbook](https://qiskit.org/textbook/preface.html)
- [IBM Quantum Experience](https://quantum-computing.ibm.com/)

## License

[Specify your license here]

## Acknowledgments

- IBM Quantum team for developing Qiskit
- The quantum computing community for advancing this exciting field
