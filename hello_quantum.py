#!/usr/bin/env python3

# Import necessary Qiskit modules
from qiskit import QuantumCircuit, transpile
from qiskit.providers.basic_provider import BasicSimulator
from qiskit.visualization import plot_histogram, plot_bloch_multivector, plot_bloch_vector
from qiskit_aer import AerSimulator, StatevectorSimulator
import numpy as np
import matplotlib.pyplot as plt


def create_circuit():
    # Create a quantum circuit with 1 qubit and 1 classical bit
    qc = QuantumCircuit(1, 1)
    
    # Add a Hadamard gate to put the qubit in superposition
    qc.h(0)
    
    # Measure the qubit
    qc.measure(0, 0)
    
    return qc


def run_simulation(circuit, shots=1000):
    # Simulate the circuit
    simulator = BasicSimulator()
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=shots)
    result = job.result()
    
    # Get the counts (measurement results)
    counts = result.get_counts()
    
    return counts


def get_statevector():
    # Create a circuit without measurement to show the state
    qc_state = QuantumCircuit(1)
    qc_state.h(0)
    
    # Use the statevector simulator to get the state
    statevector_simulator = StatevectorSimulator()
    statevector_job = statevector_simulator.run(transpile(qc_state, statevector_simulator))
    statevector_result = statevector_job.result()
    
    # Get the statevector
    return statevector_result.get_statevector()


def visualize_bloch_sphere(filename='bloch_sphere.png'):
    # For |+⟩ state (after Hadamard), the Bloch vector is [1,0,0]
    bloch_vector = [1, 0, 0]
    
    # Create and save the Bloch sphere visualization
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot using Qiskit's built-in function
    plot_bloch_vector(bloch_vector, title="Qubit State after Hadamard Gate", ax=ax)
    
    # Save the figure
    plt.savefig(filename)
    print(f"Bloch sphere visualization saved as '{filename}'")


def main():
    print("=== Qiskit Hello World ===\n")
    
    # Create and display the circuit
    circuit = create_circuit()
    print("Quantum Circuit:")
    print(circuit)
    
    # Run the simulation and display results
    counts = run_simulation(circuit)
    print("\nMeasurement Results:")
    print(counts)
    
    try:
        # Get and display the statevector
        statevector = get_statevector()
        print("\nStatevector:")
        print(statevector)
        
        # Visualize the state on the Bloch sphere
        print("\nVisualizing the state on the Bloch sphere...")
        visualize_bloch_sphere()
        
        print("\nQiskit Hello World completed successfully!")
        
    except Exception as e:
        print(f"\nVisualization not available: {e}")
        print("\nQiskit Hello World completed successfully!")


if __name__ == "__main__":
    main()
