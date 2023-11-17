# Discrete Mathematics: Graph Generator Project

## Overview
This project is a part of the Peer Group Summative for the Discrete Mathematics course facilitated by Alexandra Rogers at ALU. Our team, consisting of Samuel Munguti, Ahmed Mohamed, Ednah Akoth, Abraham Diress, and Jeremiah Ater, developed a Python program to generate simple undirected graphs and analyze their properties.

### Project Goals
1. **Graph Generation**: Write a Python program to randomly generate simple undirected graphs with 10 vertices.
2. **Graph Analysis**: Determine if the generated graph is connected and if it contains an Euler circuit.
3. **Probability Estimation**: Estimate the probability of a simple graph with 10 vertices having an Euler circuit, given that the graph is connected.

## Repository Link
[Graph Generator Project on GitHub](https://github.com/Ahmed-ALU/Graphs_Generator_Peer-Group-Summative-Project)

## Implementation Details
1. **Graph Generation**: We utilized Python lists and arrays to create adjacency matrices representing the graphs. An adjacency matrix is a square matrix used to represent a finite graph, with the elements indicating whether pairs of vertices are adjacent.
   
2. **Connected Graph Determination**: We applied depth-first search (DFS) to determine if the graph is connected. DFS is a graph traversal method that explores as far as possible along each branch before backtracking.

3. **Euler Circuit Generation**: A graph has an Euler circuit if all vertices have an even degree and are connected. Our program identifies such graphs and outputs the Euler circuit.

4. **Probability Calculation**: The probability of a graph having an Euler circuit is calculated based on the frequency of Euler circuits in multiple graph generations.

## Challenges and Learning Outcomes
- Generating adjacency matrices efficiently while ensuring the properties of undirected simple graphs.
- Implementing DFS in Python to check graph connectivity.
- Identifying and generating Euler circuits in graphs.
- Estimating probabilities through empirical methods.

## Additional Notes
- Running the program multiple times might be necessary due to the complexity of generating Euler circuits in randomly generated graphs.
- Detailed code for the probability estimation can be found in the [probability.py](https://github.com/Samuelwanza/Graphs_Generator_Peer-Group-Summative-Project/blob/main/probability.py) file in our repository.

## Conclusion
This project allowed us to apply discrete mathematics concepts practically, particularly in graph theory, and deepen our understanding of Python programming for mathematical applications.
