# Maze Solver

A Python-based maze generator and solver with real-time visualization built using **Tkinter**.  
The project demonstrates core concepts in **algorithm design, recursion, backtracking, and graphical programming**.

---

## Features

- **Maze generation** using recursive backtracking (depth-first search).  
- **Maze solving** using recursive DFS with backtracking.  
- **Step-by-step animation** of both generation and solving.  
- **Visualization** with `Tkinter`: walls, open paths, and solver moves (red for forward steps, gray for backtracking).  
- **Deterministic runs** when a seed is specified for reproducibility.  
- **Simple structure**: clean separation of logic (`maze.py`) and visualization (`graphics.py`).  

---

## Project structure

maze-solver/

├── main.py → *Program entry point*

├── maze.py → *Maze generation & solving logic*

├── graphics.py → *Visualization layer (Tkinter window, drawing primitives, Cell class)*

├── tests.py → *Unit tests (basic structure verification)*

├── run.sh → *Helper script to run the project*

├── test.sh → *Helper script to run tests*

└── README.md → *Project documentation*

---

## How to run

### Prerequisites
- Python 3.10+ (earlier versions may work but untested)
- Tkinter (bundled with most Python distributions)

### Run the demo
```bash
# Using the helper script
./run.sh
```
```bash
# Or directly with Python
python3 main.py
```
By default:
Window size: 1280x720
Maze grid: 15 x 15
Cell size: 35 x 35 pixels
RNG seed: 0 (deterministic maze)
Close the window to exit.

### Run tests
```bash
./test.sh
```
or

```bash
python3 -m unittest discover
```
## Algorithms
### Maze Generation
- Uses recursive backtracking:
  - Start from the entrance(0, 0)
  - Randomly carve passages to unvisited neighbouring cells
  - Backtrack when stuck until the grid is fully connected and a continuous path exists
- Opens:
  - Top wall of (0, 0) as the entrance
  - Bottom wall of (last column, last row) as the exit
### Maze Solving
- Uses depth-first search with backtracking:
  - Marks each visited cell
  - Draws a red line for moves into new cells
  - Draws a gray line when backtracking
  - Completes when reaching exit (last column, last row)

## Parameters
Currently, parameters are set in main.py:
```python
win = Window(1280, 720)
maze = Maze(0.025 * 720, 0.025 * 1280, 15, 15, 35, 35, win, seed=0)
# maze.solve()   # Uncomment to solve
```
You can tweak:
- Window size (width, height)
- Number of rows/columns
- Cell size
- Random Seed
- Enable/Disable solving
