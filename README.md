# Linear Algebra Studio

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ma1522-linear-algebra)](https://pypi.org/project/ma1522-linear-algebra/)
[![PyPI - Version](https://img.shields.io/pypi/v/ma1522-linear-algebra)](https://pypi.org/project/ma1522-linear-algebra/)
[![GitHub License](https://img.shields.io/github/license/yeeshin504/linear-algebra)](https://github.com/YeeShin504/linear-algebra/blob/master/LICENSE.txt)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/ma1522-linear-algebra)](https://pypistats.org/packages/ma1522-linear-algebra)
[![codecov](https://codecov.io/github/YeeShin504/linear-algebra/graph/badge.svg?token=2TJ7RSIDOI)](https://codecov.io/github/YeeShin504/linear-algebra)

A modern, interactive Web GUI for the [ma1522-linear-algebra](https://github.com/YeeShin504/linear-algebra) library.

This project provides a user-friendly graphical interface for performing symbolic linear algebra operations, making it accessible to users without Python programming knowledge.

## Credits

**Original Library & Algorithms**: [YeeShin504](https://github.com/YeeShin504) and contributors.
This project builds upon their robust `ma1522` library to provide the underlying mathematical computations.
I would also like to thank [@DenseLance](https://github.com/DenseLance) for his contributions.

## GUI Features

- **Interactive Matrix Grid**: Input matrices easily using a dynamic grid that resizes automatically.
- **Symbolic Computation**: exact results for RREF, Determinant, Inverse, Eigenvalues, and more.
- **Advanced Operations**: Support for SVD (Singular Value Decomposition) and Diagonalization.
- **Equivalent Statements**: Instantly analyze matrix properties (Rank, Invertibility, etc.) based on the MA1522 syllabus.
- **Flexible Input**: Supports Python lists, MATLAB syntax, and LaTeX.
- **Beautiful Output**: Results are rendered in standard mathematical notation using LaTeX.

## Library Features

1. Import matrices directly from $\rm\LaTeX$ or string/list representations.
2. Step-by-step workings for most algorithms (including LU Factorisation, SVD, QR, diagonalization, and more).
3. Enhanced symbolic matrix class with:
    - Matrix creation from lists, $\rm\LaTeX$, or random values.
    - Matrix decompositions: REF, RREF, LU, QR, SVD, diagonalization.
    - Vector space operations: orthogonalization, projections, basis manipulation, subspace intersection, and more.
    - Eigenvalue/eigenvector computations and characteristic polynomials.
    - Custom pretty-printing and $\rm\LaTeX$ formatting, including augmented matrices.
    - Support for both exact symbolic and numerical computations.
    - Utilities for displaying results in Jupyter/IPython or standard Python.
4. Follows MA1522 syllabus conventions for linear algebra and provides detailed, educational output.
5. Rich set of custom types for representing decompositions, solutions, and factorizations.

## Getting Started

### Prerequisites

- Python 3.10+
- This project is best supported with Python 3.10+. You can download Python from [here](https://www.python.org/downloads/).

### Installation

1.  Clone this repository.
2.  Install the dependencies:
    Using **uv** (Recommended):
    ```bash
    uv sync
    ```
    Alternatively, using **pip**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

### Running the GUI

1.  Start the local server:
    ```bash
    # From the project root directory
    ./run.sh
    ```

2.  Open your web browser and navigate to:
    [http://127.0.0.1:8000](http://127.0.0.1:8000)

## GUI Usage

1.  **Enter a Matrix**: Use the grid to type in numbers or symbolic expressions (e.g., `sqrt(2)`). You can also switch to text mode to paste Python lists.
2.  **Select an Operation**: Click any button in the control panel (e.g., "RREF", "Eigenvalues", "SVD").
3.  **View Results**: The result will appear below in formatted LaTeX.
4.  **Check Properties**: Click "Show Equivalent Statements" to see a categorized list of the matrix's properties.

## Library Usage

```python
# Create Matrix objects
from ma1522.symbolic import Matrix
A = Matrix([[1, 2, 3],
            [4, 5, 5],
            [7, 8, 9]])

b = Matrix([[1], 
            [2], 
            [3]])

# Join matrices along the columns via `row_join`. 
augmented_matrix = A.aug_line().row_join(b)

# `aug_line` adds a visual line that can be seen using `display`
# In Jupyter/IPython: display(augmented_matrix)

# Solution to the matrix equation Ax = b can be found using `solve`.
print(A.solve(rhs=b))

# Alternatively, the full steps with LU Factorisation can be found using `ref` with the appropriate options.
augmented_matrix.ref(verbosity=2)
```

Documentation of more functions can be found [here](https://yeeshin504.github.io/linear-algebra/api/symbolic).

More usage examples can be found under [tutorials](https://yeeshin504.github.io/linear-algebra/tutorials/tutorial).

Live demonstration of the library can be found [here](https://yeeshin504.github.io/linear-algebra/live/demo).

### Offline Documentation

An offline version of the documentation is available for download from the [Releases](https://github.com/YeeShin504/linear-algebra/releases) page.

To use the offline documentation:

1. Download `linear-algebra-docs-offline.zip` from the latest release
2. Extract the ZIP to a folder
3. Open `index.html` in your browser

A quick reference guide is also available as a function in the library:
```python
from ma1522 import sympy_commands
sympy_commands()
```
