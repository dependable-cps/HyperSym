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


