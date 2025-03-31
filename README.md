# Transport Optimization Project

This project implements a linear programming model to optimize the transportation of high-performance engines from multiple manufacturers to various destination countries. The model minimizes transportation cost while meeting production, demand, and storage constraints.

## Project Overview

- **Manufacturers:** Ferrari Motors, Mercedes Engines Ltd., and Renault Racing Tech.
- **Countries:** USA, Italy, Germany, France, and Japan.
- **Objective:** Minimize the total transportation cost.
- **Constraints:** 
  - Manufacturing capacity limits.
  - Demand (and storage) requirements.
  - Shipping container storage capacities.

## Files

- `transport_optimization.py`: Python script containing the LP model using PuLP.
- `requirements.txt`: List of Python dependencies.
- `.gitignore`: Files/folders to ignore in version control.
- `LICENSE`: MIT License file.

## Setup and Execution

1. **Clone or download the repository.**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
