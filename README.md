# HyperSYM: An SMT-Based Model Checker Tool for HyperTWTL
This repository contains HyperSYM,an automated tool for verifying and synthesizing Hyperproperties for Time Window Temporal Logic (HyperTWTL) specifications.

### Clone this repository:
```sh
git clone https://github.com/dependable-cps/HyperSym
cd HyperSym
```
## Overview
The HyperSYM tool inputs a HyperTWTL formula and a model as input. Our tool converts the model into a collection of models, where m is the number of quantified traces in the HyperTWTL formula. The inputs are then parsed and encoded as a first-order logic formula, which is then unrolled to a bound, computed from the input formula. The first-order logic formula is then fed into an off-the-shelf SMT solver such as Z3 to determine its satisfiability.

## Project Structure

The project is organized into the following directories:

* **src/**: Contains the core Python 3 source code for the HyperSYM tool.
* **files/**: Houses TypeScript (Ts) files and model files used throughout the project.
* **plots/**: Stores the generated synthesis output plots for visualization.
* **main.py**: The main entry point for running the tool.

## Build HyperSym
### Dependencies

We require the following dependencies:

* **Python 3.8** (tested with version 3.8.3)
* **Matplotlib** (tested with version 3.8.3)
* **Z3-solver** (tested with version 4.13.0.0)

## Build HyperSym
To build HyperSym run the following (when in the main directory of this repository).
```sh
cd HyperSym
python main.py
```
## Input to HyperSym
The user can provide input via the `dts.txt` file to configure the parameters and states required by the program, and a `text` file to specify the formula to be run.

* The `dts.txt` file should be formatted as follows:

### Parameters

- **N**: The size of the grid or number of states (e.g., `N : 10;`).
- **Initial States**: The initial states of the system, separated by commas (e.g., `Initial States : s_0_1, s_0_2, s_0_3, s_0_4;`).
- **Obstacles**: The states that are considered obstacles, separated by commas (e.g., `Obstacles : s_0_5, s_0_6, s_0_7, s_0_8, s_0_9, ...;`).
- **Goal States**: The target or goal states, separated by commas (e.g., `Goal States : s_9_7, s_9_8, s_9_9, s_8_7, s_8_8, s_8_9;`).
- - **synthesis**: This command initiates the synthesis process based on the provided input states and parameters(or verification)
- **Intermediate States**: The states that act as intermediate checkpoints, separated by commas (e.g., `Intermediate States : s_5_2, s_5_6;`).

### Formula File (`text`)

The `text` file should contain the formula you want to run. The syntax for the formula can be found in the `formula_syntax` file.

