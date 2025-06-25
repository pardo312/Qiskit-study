#!/usr/bin/env python3
"""
Grover's Search Algorithm Implementation

This script demonstrates Grover's quantum search algorithm using Qiskit:
- Creates a superposition of all possible states
- Applies an oracle to mark the target state
- Uses amplitude amplification to increase the probability of the target state
- Measures to find the marked item with high probability
"""

# Import necessary Qiskit modules
from qiskit import QuantumCircuit, transpile
from qiskit.providers.basic_provider import BasicSimulator
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator, StatevectorSimulator
import matplotlib.pyplot as plt
import numpy as np
import math


def initialize_s(qc, qubits):
    """
    Apply Hadamard gates to all qubits to create a uniform superposition.
    
    Args:
        qc (QuantumCircuit): The quantum circuit
        qubits (list): List of qubits to apply Hadamard gates to
    """
    for q in qubits:
        qc.h(q)
    return qc


def create_oracle(target_state):
    """
    Create an oracle function that marks the target state by flipping its phase.
    
    Args:
        target_state (str): Binary string representing the target state to mark
        
    Returns:
        QuantumCircuit: Oracle circuit that marks the target state
    """
    n = len(target_state)
    oracle_qc = QuantumCircuit(n)
    
    # Apply X gates to qubits where the target bit is 0
    # This converts the target state to all 1's
    for qubit, bit in enumerate(target_state):
        if bit == '0':
            oracle_qc.x(qubit)
    
    # Apply multi-controlled Z gate
    # For 2 qubits, we can use CZ
    if n == 2:
        oracle_qc.cz(0, 1)
    else:
        # For more qubits, we use a multi-controlled Z implementation
        # Add ancilla qubit
        oracle_qc.mcx(list(range(n-1)), n-1)
        oracle_qc.z(n-1)
        oracle_qc.mcx(list(range(n-1)), n-1)
    
    # Apply X gates again to revert the qubits
    for qubit, bit in enumerate(target_state):
        if bit == '0':
            oracle_qc.x(qubit)
    
    return oracle_qc


def create_diffusion_operator(n_qubits):
    """
    Create the diffusion operator (Grover's diffusion) that amplifies the amplitude of the marked state.
    
    Args:
        n_qubits (int): Number of qubits
        
    Returns:
        QuantumCircuit: Diffusion operator circuit
    """
    qc = QuantumCircuit(n_qubits)
    
    # Apply H gates to all qubits
    for qubit in range(n_qubits):
        qc.h(qubit)
    
    # Apply X gates to all qubits
    for qubit in range(n_qubits):
        qc.x(qubit)
    
    # Apply multi-controlled Z gate
    # For 2 qubits, we can use CZ
    if n_qubits == 2:
        qc.cz(0, 1)
    else:
        # For more qubits, we use a multi-controlled Z implementation
        qc.h(n_qubits-1)
        qc.mcx(list(range(n_qubits-1)), n_qubits-1)
        qc.h(n_qubits-1)
    
    # Apply X gates to all qubits
    for qubit in range(n_qubits):
        qc.x(qubit)
    
    # Apply H gates to all qubits
    for qubit in range(n_qubits):
        qc.h(qubit)
    
    return qc


def create_grovers_circuit(n_qubits, target_state, num_iterations=1):
    """
    Create the complete Grover's algorithm circuit.
    
    Args:
        n_qubits (int): Number of qubits
        target_state (str): Binary string representing the target state
        num_iterations (int): Number of Grover iterations to perform
        
    Returns:
        QuantumCircuit: Complete Grover's algorithm circuit
    """
    # Create quantum circuit with n qubits and n classical bits
    qc = QuantumCircuit(n_qubits, n_qubits)
    
    # Initialize qubits in superposition
    qc = initialize_s(qc, range(n_qubits))
    
    # Get the oracle and diffusion operator
    oracle = create_oracle(target_state)
    diffusion = create_diffusion_operator(n_qubits)
    
    # Perform Grover iterations
    for _ in range(num_iterations):
        # Apply oracle
        qc = qc.compose(oracle)
        
        # Apply diffusion operator
        qc = qc.compose(diffusion)
    
    # Measure all qubits
    qc.measure(range(n_qubits), range(n_qubits))
    
    return qc


def calculate_optimal_iterations(n_qubits, num_solutions=1):
    """
    Calculate the optimal number of Grover iterations.
    
    Args:
        n_qubits (int): Number of qubits
        num_solutions (int): Number of solutions in the search space
        
    Returns:
        int: Optimal number of iterations
    """
    N = 2**n_qubits  # Size of the search space
    # Optimal number of iterations is approximately (pi/4) * sqrt(N/M)
    # where M is the number of solutions
    optimal = (math.pi/4) * math.sqrt(N/num_solutions)
    return int(optimal)


def run_grovers_algorithm(n_qubits, target_state, shots=1024):
    """
    Run Grover's algorithm and return the results.
    
    Args:
        n_qubits (int): Number of qubits
        target_state (str): Binary string representing the target state
        shots (int): Number of times to run the simulation
        
    Returns:
        dict: Counts of measurement results
    """
    # Calculate optimal number of iterations
    optimal_iterations = calculate_optimal_iterations(n_qubits)
    print(f"Optimal number of Grover iterations: {optimal_iterations}")
    
    # Create Grover's circuit
    grover_circuit = create_grovers_circuit(n_qubits, target_state, optimal_iterations)
    
    # Simulate the circuit
    simulator = BasicSimulator()
    compiled_circuit = transpile(grover_circuit, simulator)
    job = simulator.run(compiled_circuit, shots=shots)
    result = job.result()
    
    # Get the counts
    counts = result.get_counts()
    
    return grover_circuit, counts


def visualize_results(circuit, counts):
    """
    Visualize the circuit and measurement results.
    
    Args:
        circuit (QuantumCircuit): The quantum circuit
        counts (dict): Counts of measurement results
    """
    # Print the circuit
    print("Grover's Algorithm Circuit:")
    print(circuit)
    
    # Plot the histogram of measurement results
    plt.figure(figsize=(12, 6))
    plot_histogram(counts, title="Grover's Algorithm Results")
    plt.savefig('grovers_results.png')
    print("Results histogram saved as 'grovers_results.png'")


def explain_grovers_algorithm():
    """
    Provide an explanation of Grover's algorithm.
    """
    explanation = """
Grover's Algorithm Explanation:
------------------------------
Grover's algorithm is a quantum algorithm for searching an unsorted database with a quadratic speedup compared to classical algorithms.

Key Components:

1. Initialization:
   - Start with all qubits in |0⟩ state
   - Apply Hadamard gates to create a superposition of all possible states
   - This gives each state an equal amplitude of 1/√N

2. Oracle (Phase Flip):
   - The oracle marks the target state by flipping its phase
   - It applies a conditional phase shift of -1 to the target state
   - This doesn't change the probability of measuring any state yet

3. Diffusion Operator (Amplitude Amplification):
   - Performs "inversion about the mean"
   - Increases the amplitude of the marked state
   - Decreases the amplitude of all other states
   - This is the key step that makes the target state more likely to be measured

4. Iterations:
   - Repeat the oracle and diffusion steps √N times
   - Each iteration gradually increases the probability of the target state
   - Too few iterations: target not amplified enough
   - Too many iterations: probability starts decreasing again

5. Measurement:
   - After the optimal number of iterations, measure all qubits
   - The target state will be measured with high probability

Quantum Advantage:
- Classical search: O(N) operations
- Quantum search with Grover's: O(√N) operations
- This quadratic speedup is proven to be optimal for quantum search

Applications:
- Database searching
- Finding solutions to constraint satisfaction problems
- Speeding up brute-force attacks in cryptography
- As a subroutine in other quantum algorithms
"""
    print(explanation)


def main():
    """
    Main function to run Grover's algorithm.
    """
    print("=== Grover's Search Algorithm ===\n")
    
    # Set the number of qubits and target state
    n_qubits = 3
    target_state = '101'  # The state we're searching for
    
    print(f"Search space size: {2**n_qubits} items")
    print(f"Target state: |{target_state}⟩")
    
    # Run Grover's algorithm
    circuit, counts = run_grovers_algorithm(n_qubits, target_state)
    
    # Visualize the results
    visualize_results(circuit, counts)
    
    # Explain the algorithm
    explain_grovers_algorithm()
    
    print("\nGrover's Algorithm demonstration completed successfully!")


if __name__ == "__main__":
    main()
