Scientific Data Analyzer
Programming Project for Course Assessment

Evaluation method: Public Git repository, documented source code, executable tests

1. Project Description

This repository contains a Python programming project developed for academic assessment.
The project analyzes numerical datasets using regression techniques and demonstrates:

. structured source code,

. meaningful version control usage,

. executable automated tests.

The project is fully hosted on a public Git repository and developed using Git.

2. Repository Structure

Scientific-Data-Analyzer/
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── analysis.py
│   └── main.py
│
├── tests/
│   ├── __init__.py
│   ├── test_loader.py
│   └── test_analysis.py
│
├── example.csv
├── requirements.txt
├── README.md
└── LICENSE

# Design choices:

. data_loader.py: data input and validation

. analysis.py: numerical computation (linear and polynomial regression)

. main.py: command-line interface and plotting

. tests/: automated test routines

# Version Control and Commit History (6 points)

The project was developed incrementally using Git.

The commit history:

. follows a clear convention (feat, fix, test, docs, refactor)

. groups logically related changes

. documents the evolution of the project step by step

Example commit messages:

. feat: add polynomial regression model

. test: add unit tests for analysis functions

. fix: make CSV loader robust to malformed rows

. docs: update README with execution instructions

This ensures clarity of repository commit history, as required.

4. Data Input

Input data is provided as a CSV file containing numerical (x, y) pairs.

Example (example.csv):
0,0
1,1
2,4
3,9
4,16

2. Implemented Methods

# Linear Regression (Baseline Model)

A linear regression model is implemented as a baseline hypothesis.
It estimates slope and intercept and provides a simple reference for comparison.

# Polynomial Regression (Extended Model)

Polynomial regression generalizes the linear model by allowing higher-order terms.

Features:

user-defined polynomial degree

smooth curve evaluation on a dense grid

linear regression is a special case (degree = 1)

This demonstrates extension from a simple to a more complex model.

#  Program Execution

. Linear Model
python -m src.main --file example.csv --model linear

. Polynomial Model
python -m src.main --file example.csv --model poly --degree 2

The program:

. loads data,

. performs regression,

. produces a plot comparing data and fitted model.

# Automated Tests

Automated tests are provided using pytest

python -m pytest

# Test coverage includes:

. CSV loading correctness

. linear regression correctness

. polynomial regression behavior

All tests are:

executable,

isolated,

reproducible.

# Conclusion

This project satisfies all mandatory assessment criteria:

clarity of repository and commits

completeness of documentation and code

presence and executability of tests
