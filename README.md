# Artificial Intelligence (AI) Practicals

## 📌 Introduction

This repository contains practical implementations of important Artificial Intelligence (AI) algorithms and problem-solving techniques. These practicals help us understand how AI systems search for solutions, solve puzzles, make decisions, and apply knowledge to solve real-world problems.

## 🎯 Objectives

- Understand fundamental AI search algorithms.
- Implement Breadth First Search (BFS) and Depth First Search (DFS).
- Solve the Water Jug Problem using state-space search.
- Understand the 8 Puzzle Problem.
- Implement the A* Search Algorithm.
- Learn the Hill Climbing Algorithm.
- Understand decision-making using the Minimax Algorithm.
- Develop a basic Expert System.

## 📚 List of Practicals

### 1. Breadth First Search (BFS)

**Description:**

Breadth First Search (BFS) is an uninformed search algorithm that explores a graph level by level. It visits all neighboring nodes before moving to the next level. BFS uses a queue data structure to maintain the order of nodes to be explored.

**Aim:**
To implement the Breadth First Search algorithm to traverse a graph.

**Applications:**
- Finding the shortest path in an unweighted graph.
- Network broadcasting.
- Web crawling.

### 2. Depth First Search (DFS)

**Description:**

Depth First Search (DFS) is an uninformed search algorithm that explores a path as deeply as possible before backtracking. It uses a stack data structure or recursion to traverse a graph.

**Aim:**
To implement the Depth First Search algorithm for graph traversal.

**Applications:**
- Maze solving.
- Cycle detection in graphs.
- Path exploration.

### 3. Water Jug Problem

**Description:**

The Water Jug Problem is a classical AI problem in which two jugs of different capacities are used to measure a specific quantity of water. The problem is solved by defining states and applying operations such as filling, emptying, and transferring water between jugs.

**Aim:**
To solve the Water Jug Problem using state-space search.

**Applications:**
- Understanding state-space representation.
- Learning search strategies.
- Solving constraint-based problems.

### 4. 8 Puzzle Problem

**Description:**

The 8 Puzzle Problem consists of a 3 × 3 board containing eight numbered tiles and one empty space. The objective is to arrange the tiles into a specified goal state by moving tiles into the empty space.

**Aim:**
To solve the 8 Puzzle Problem using AI search techniques.

**Applications:**
- Understanding state-space search.
- Learning heuristic search.
- Exploring problem-solving strategies.

### 5. A* Search Algorithm

**Description:**

A* is an informed search algorithm that finds a path from a starting state to a goal state using both the actual cost and the estimated cost to reach the goal. It uses the evaluation function:

**f(n) = g(n) + h(n)**

Where:
- **g(n):** Actual cost from the start node to node n.
- **h(n):** Estimated cost from node n to the goal.
- **f(n):** Estimated total cost of the path through node n.

**Aim:**
To implement the A* Search Algorithm for finding an optimal path.

**Applications:**
- GPS navigation.
- Robotics.
- Pathfinding in games.

### 6. Hill Climbing Algorithm

**Description:**

Hill Climbing is a local search algorithm that continuously moves toward a neighboring state with a better evaluation value. It stops when no neighboring state offers an improvement. It may get stuck at local maxima, plateaus, or ridges.

**Aim:**
To implement the Hill Climbing Algorithm for optimization problems.

**Applications:**
- Optimization problems.
- Scheduling.
- Feature selection in machine learning.

### 7. Minimax Algorithm

**Description:**

Minimax is a decision-making algorithm used in two-player games. It assumes that one player tries to maximize the score while the opponent tries to minimize it. The algorithm explores possible moves to select the best move under optimal play.

**Aim:**
To implement the Minimax Algorithm for decision-making in a game.

**Applications:**
- Tic-Tac-Toe.
- Chess.
- Other two-player strategy games.

### 8. Expert System

**Description:**

An Expert System is an AI program that uses stored knowledge and predefined rules to solve problems in a specific domain. It generally consists of a knowledge base, an inference engine, and a user interface.

**Aim:**
To develop a basic Expert System using knowledge-based rules.

**Applications:**
- Medical decision support.
- Fault diagnosis.
- Recommendation and advisory systems.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Subject:** Artificial Intelligence
- **Concepts:** Search Algorithms, State-Space Search, Heuristic Search, Optimization, Game Playing, and Knowledge-Based Systems.

## 🚀 How to Run

1. Install Python on your computer.
2. Clone or download this repository.
3. Open the project folder in a code editor.
4. Run the required Python practical using the terminal.

Example:

```bash
python bfs.py
```

Replace `bfs.py` with the filename of the practical you want to execute.

## 📖 Learning Outcomes

After completing these practicals, students will be able to:

- Explain basic AI concepts and algorithms.
- Represent problems using states and state spaces.
- Apply search algorithms to solve problems.
- Use heuristic functions to guide search.
- Understand AI-based game-playing strategies.
- Build a simple rule-based Expert System.

## 👨‍🎓 Conclusion

These practicals provide a foundation in Artificial Intelligence by demonstrating search techniques, problem-solving methods, optimization strategies, game-playing algorithms, and knowledge-based reasoning. They help students understand how AI techniques can be applied to computational and real-world problems.

