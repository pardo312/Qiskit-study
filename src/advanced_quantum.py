#!/usr/bin/env python3
"""
Advanced Qiskit Example

This script demonstrates more complex quantum computing concepts using Qiskit:
- Multi-qubit circuits
- Entanglement with CNOT gates
- Phase manipulation with S and T gates
- Quantum interference
- Bell state creation
- Advanced visualization
"""

# Import necessary Qiskit modules
from qiskit import QuantumCircuit, transpile
from qiskit.providers.basic_provider import BasicSimulator
from qiskit.visualization import plot_histogram, plot_bloch_multivector, plot_state_city
from qiskit_aer import AerSimulator, StatevectorSimulator
import numpy as np
import matplotlib.pyplot as plt


def create_advanced_circuit():
    qc = QuantumCircuit(3, 3)
    
    # puerta de neymar
    qc.h(0)
    qc.h(1)
    
    # CNOT gate => entrelaza los qbits 0 y 1
    qc.cx(0, 1)
    
    # S gate => Rotación de fase de 90 grados en el qbit 0
    # Fase es como otra propiedad del quark que nos sirve para 
    # controlar interferencia entre estados del qubit
    qc.s(0)
    
    # otra cnot pero pa entrelazar el qbit 1 y 2
    qc.cx(1, 2)
    
    # T gate => Rotación de fase de 45 grados en el qbit 1
    qc.t(1)
    
    # puerta de neymar para crear interferencia
    qc.h(0)
    
    # 👁️ Medimos
    qc.measure([0, 1, 2], [0, 1, 2])
    
    return qc


def run_simulation(circuit, shots=1000):
    """
    Run a quantum circuit on a simulator.
    
    Args:
        circuit (QuantumCircuit): The quantum circuit to simulate
        shots (int): Number of times to run the simulation
        
    Returns:
        dict: Counts of measurement results
    """
    # Simulate the circuit
    simulator = BasicSimulator()
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=shots)
    result = job.result()
    
    # Get the counts (measurement results)
    counts = result.get_counts()
    
    return counts


def get_statevector(circuit_without_measurement):
    """
    Get the statevector of a circuit before measurement.
    
    Args:
        circuit_without_measurement (QuantumCircuit): Circuit without measurement operations
        
    Returns:
        statevector: The quantum state of the circuit
    """
    # Use the statevector simulator to get the state
    statevector_simulator = StatevectorSimulator()
    statevector_job = statevector_simulator.run(
        transpile(circuit_without_measurement, statevector_simulator)
    )
    statevector_result = statevector_job.result()
    
    # Get the statevector
    return statevector_result.get_statevector()


def create_circuit_without_measurement():
    """
    Create the same advanced circuit but without measurement operations.
    
    Returns:
        QuantumCircuit: The circuit without measurement operations
    """
    # Create a quantum circuit with 3 qubits and no classical bits
    qc = QuantumCircuit(3)
    
    # Apply Hadamard gates to create superposition on qubits 0 and 1
    qc.h(0)
    qc.h(1)
    
    # Entangle qubits 0 and 1 with CNOT (creating a Bell state)
    qc.cx(0, 1)
    
    # Apply phase shift to qubit 0 with S gate (90-degree phase)
    qc.s(0)
    
    # Entangle qubits 1 and 2
    qc.cx(1, 2)
    
    # Apply phase shift to qubit 1 with T gate (45-degree phase)
    qc.t(1)
    
    # Apply Hadamard to qubit 0 to demonstrate interference
    qc.h(0)
    
    return qc


def visualize_results(counts, statevector):
    """
    Create and save visualizations of the quantum circuit results.
    
    Args:
        counts (dict): Measurement results
        statevector: Quantum state before measurement
    """
    # Create a figure for the histogram
    plt.figure(figsize=(12, 6))
    plot_histogram(counts, title="Measurement Results")
    plt.savefig('measurement_histogram.png')
    print("Measurement histogram saved as 'measurement_histogram.png'")
    
    # Create a figure for the statevector visualization (as a city plot)
    try:
        plt.figure(figsize=(12, 6))
        plot_state_city(statevector, title="Quantum State Visualization")
        plt.savefig('state_visualization.png')
        print("State visualization saved as 'state_visualization.png'")
    except Exception as e:
        print(f"Could not create state visualization: {e}")
    
    # Try to create a Bloch multivector visualization
    try:
        fig = plt.figure(figsize=(15, 5))
        plot_bloch_multivector(statevector, title="Bloch Sphere Representation")
        plt.savefig('bloch_multivector.png')
        print("Bloch multivector visualization saved as 'bloch_multivector.png'")
    except Exception as e:
        print(f"Could not create Bloch multivector: {e}")


def explain_circuit():
    """
    Provide an explanation of the quantum circuit and its expected behavior.
    """
    explanation = """
Circuit Explanation:
-------------------
1. We start with 3 qubits in the |000⟩ state.

2. Hadamard gates on qubits 0 and 1:
   - Puts them in superposition: (|0⟩ + |1⟩)/√2 for each
   - System state: (|000⟩ + |010⟩ + |100⟩ + |110⟩)/2

3. CNOT gate with qubit 0 as control and qubit 1 as target:
   - Creates entanglement between qubits 0 and 1
   - System state: (|000⟩ + |011⟩ + |100⟩ + |111⟩)/2

4. S gate on qubit 0 (90-degree phase shift):
   - Adds a phase of i to the |1⟩ state of qubit 0
   - System state: (|000⟩ + |011⟩ + i|100⟩ + i|111⟩)/2

5. CNOT gate with qubit 1 as control and qubit 2 as target:
   - Entangles qubit 2 with the already entangled pair
   - System state: (|000⟩ + |011⟩ + i|101⟩ + i|110⟩)/2

6. T gate on qubit 1 (45-degree phase shift):
   - Adds a phase of e^(iπ/4) to the |1⟩ state of qubit 1
   - Creates a more complex phase relationship

7. Hadamard gate on qubit 0:
   - Creates interference between different paths
   - Demonstrates how phases affect interference patterns

8. Measurement:
   - Collapses the quantum state
   - Due to entanglement, measuring one qubit affects the others
   - The distribution of results reveals the quantum correlations
"""
    print(explanation)


def main():
    """
    Main function to run the advanced quantum circuit example.
    """
    print("=== Advanced Quantum Circuit Example ===\n")
    
    # Create and display the circuit with measurements
    circuit = create_advanced_circuit()
    print("Quantum Circuit:")
    print(circuit)
    
    # Create the same circuit without measurements for statevector analysis
    circuit_without_measurement = create_circuit_without_measurement()
    
    # Run the simulation and display results
    counts = run_simulation(circuit)
    print("\nMeasurement Results:")
    print(counts)
    
    try:
        # Get the statevector (before measurement)
        statevector = get_statevector(circuit_without_measurement)
        print("\nStatevector (before measurement):")
        print(statevector)
        
        # Visualize the results
        print("\nCreating visualizations...")
        visualize_results(counts, statevector)
        
        # Explain the circuit
        print("\nCircuit Explanation:")
        explain_circuit()
        
        print("\nAdvanced Quantum Circuit example completed successfully!")
        
    except Exception as e:
        print(f"\nError during execution: {e}")


if __name__ == "__main__":
    main()
