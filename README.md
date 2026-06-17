# AI Snake Game: Search Algorithm Performance Analysis

## Project Overview

This project examines and compares various Artificial Intelligence search algorithms and their performance against a human player in the classic Snake Game.

The system provides an interactive dashboard where users can select different algorithms and observe how they navigate the game environment to collect food while avoiding collisions.

Algorithms implemented:

- Human Player
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- A* Search
- Hamiltonian Cycle

The project also records gameplay statistics and generates performance comparison graphs.

---

## Objectives

- Study the behavior of different AI search algorithms.
- Compare AI performance with human gameplay.
- Evaluate pathfinding efficiency and survival capability.
- Visualize algorithm performance using statistical analysis.

---

## Features

### User Interface
- Interactive dashboard
- Algorithm selection menu
- Human gameplay mode
- Pause and resume functionality
- Stop button to return to dashboard

### Artificial Intelligence
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- A* Search
- Hamiltonian Cycle Strategy

### Analytics
- Performance logging
- CSV result storage
- Comparison table generation
- Algorithm performance graphs
- Best algorithm identification

---

## Technologies Used

### Frontend
- Python
- Pygame

### Backend
- Python
- Pandas
- Matplotlib

---

## Project Structure

```text
AI-Snake-Search-Algorithms/
│
├── frontend.py
├── backend.py
├── requirements.txt
├── README.md
├── .gitignore
└── results.csv
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ai-snake-search-algorithms.git
```

Move into the project directory:

```bash
cd ai-snake-search-algorithms
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python frontend.py
```

---

## Algorithms Implemented

### Breadth-First Search (BFS)

BFS explores all neighboring nodes level by level and guarantees the shortest path when one exists.

### Depth-First Search (DFS)

DFS explores deeply into one branch before backtracking. It may not always find the shortest path.

### A* Search

A* uses a heuristic function to efficiently find near-optimal paths.

### Hamiltonian Cycle

The Hamiltonian strategy follows a cycle that visits every grid cell exactly once, maximizing survival and reducing collisions.

---

## Performance Metrics

The following metrics are recorded:

- Score
- Number of Steps
- Execution Time
- Algorithm Used

These metrics are stored in `results.csv` and used for comparison.

---

## Results

The application generates:

- Performance comparison tables
- Average score analysis
- Algorithm ranking
- Visualization graphs

---

## Future Enhancements

- Reinforcement Learning Agent
- Deep Q-Learning Snake AI
- Hybrid A* + Hamiltonian Strategy
- Embedded Graph Dashboard
- Export Results to Excel and PDF
- Advanced Analytics and Reporting

---

## Academic Use

This project was developed as part of a study:

**"Examining Various Search Algorithms in AI With Appropriate Literature and Their Performances Against a Human Agent in the Snake Game"**

The project demonstrates the practical implementation and evaluation of search algorithms in a dynamic game environment.

---

## License

This project is intended for educational and research purposes.
