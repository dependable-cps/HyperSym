# HyperSYM: An SMT-Based Model Checker Tool for HyperTWTL
This repository contains HyperSYM,an automated tool for verifying and synthesizing Hyperproperties for Time Window Temporal Logic (HyperTWTL) specifications.

1. ### Clone this repository:
```sh
git clone https://github.com/dependable-cps/HyperSym
cd HyperSym
```
2. ## Overview
The HyperSYM tool inputs a HyperTWTL formula and a model as input. Our tool converts the model into a collection of models, where m is the number of quantified traces in the HyperTWTL formula. The inputs are then parsed and encoded as a first-order logic formula, which is then unrolled to a bound, computed from the input formula. The first-order logic formula is then fed into an off-the-shelf SMT solver such as Z3 to determine its satisfiability.

## Structure
src/: Contains the source code of the HyperSYM tool (written in Python 3).
files/: Contains Ts and model files which are used by all the files.
plots/: Synthesis output plots can be seen here.
main.py: Main file to run the code.
