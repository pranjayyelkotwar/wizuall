# WizUALL Compiler Project

## Overview
WizUALL is a programming language designed for data visualization, built as part of a Compiler Construction course project. The toolchain processes WizUALL programs and data streams (from PDFs) to generate Python code that produces visualizations such as histograms, scatter plots, and line plots. The project includes a preprocessor, a compiler, and a runtime environment, targeting Python as the output language for its rich visualization libraries (e.g., Matplotlib, Seaborn).

## Features

- **Preprocessing**: Extracts labeled numeric data from PDFs into a stream.
- **Compiler**: Translates WizUALL programs (supporting vector arithmetic, assignments, conditionals, loops, external function calls, and visualization primitives) into Python code.
- **Visualization Primitives**: Supports at least six primitives: histogram, scatter, plot, reverse, slice, and cluster.
- **Flexible Input/Output**: Handles various data formats and produces visualizations as .png files.
- **Test Cases**: Includes nine test cases to validate arithmetic operations and visualizations.

## Project Structure
```
project_final/
├── examples/               # Test case .wiz and .txt files, and generated PDFs
├── outputs/                # Generated Python code and visualization outputs (.png)
├── scripts/                # Scripts to run toolchain and generate PDFs
│   ├── generate_pdf.py
│   └── run_toolchain.py
├── src/                    # Source code for the toolchain
│   ├── compiler/           # Lexer, parser, and code generator
│   ├── core/               # Toolchain integration
│   ├── preprocessor/       # PDF data extraction
│   └── runtime/            # Visualization utilities
├── tests/                  # Test cases
└── requirements.txt        # Python dependencies
```

## Setup

### Clone the Repository:
```bash
git clone https://github.com/pranjayyelkotwar/wizuall.git
cd wizuall
```

### Create a Virtual Environment (recommended):
```bash
python -m venv cc_project
source cc_project/bin/activate  # On macOS/Linux
cc_project\Scripts\activate     # On Windows
```

### Install Dependencies:
```bash
pip install -r requirements.txt
```

Required packages: ply, PyPDF2, reportlab, matplotlib, numpy, seaborn, scikit-learn.

### Verify Test Case Files:
Ensure the examples/ directory contains:
- test_case_1.wiz to test_case_9.wiz
- test_case_1_data.txt to test_case_9_data.txt

## Generating PDFs
Test case data files (.txt) need to be converted to PDFs for preprocessing. Run:
```bash
cd scripts
python generate_pdf.py
```

This generates test_case_1_data.pdf to test_case_9_data.pdf in examples/.

## Running Test Cases

### Individual Test Case
To run a specific test case (e.g., Test Case 2):
```bash
cd wizuall
python scripts/run_toolchain.py examples/test_case_2_data.pdf examples/test_case_2.wiz
```

**Output:** 
- outputs/output.py: Generated Python code.
- outputs/histogram.png, outputs/scatter.png, outputs/plot.png (for visualization test cases).

### All Test Cases
To run all test cases (1–9):
```bash
python scripts/run_toolchain.py
```

**Output:**
- Generated Python code for all test cases
- Visualization files (.png) for test cases with visualization primitives.

## Visualization Outputs
Visualization outputs (e.g., histogram.png, scatter.png, plot.png) are saved in the `outputs/` directory.

### Test Case Details:
- **Test Case 1**: No visualizations (arithmetic only)
- **Test Case 2**: histogram.png, scatter.png, plot.png
- **Test Case 3**: No visualizations (arithmetic only)
- **Test Case 4**: histogram.png, plot.png
- **Test Case 5**: scatter.png
- **Test Case 6**: histogram.png, scatter.png, plot.png