WizUALL Compiler Project
Overview
WizUALL is a programming language designed for data visualization, built as part of a Compiler Construction course project. The toolchain processes WizUALL programs and data streams (from PDFs) to generate Python code that produces visualizations such as histograms, scatter plots, and line plots. The project includes a preprocessor, a compiler, and a runtime environment, targeting Python as the output language for its rich visualization libraries (e.g., Matplotlib, Seaborn).
Features

Preprocessing: Extracts labeled numeric data from PDFs into a stream.
Compiler: Translates WizUALL programs (supporting vector arithmetic, assignments, conditionals, loops, external function calls, and visualization primitives) into Python code.
Visualization Primitives: Supports at least six primitives: histogram, scatter, plot, reverse, slice, and cluster.
Flexible Input/Output: Handles various data formats and produces visualizations as .png files.
Test Cases: Includes nine test cases to validate arithmetic operations and visualizations.

Project Structure
project_final/
├── examples/               # Test case .wiz and .txt files, and generated PDFs
├── outputs/                # Generated Python code and visualization outputs (.png)
├── scripts/                # Scripts to run toolchain and generate PDFs
│   ├── generate_test_pdfs.py
│   ├── run_all_tests.py
│   └── run_toolchain.py
├── src/                    # Source code for the toolchain
│   ├── compiler/           # Lexer, parser, and code generator
│   ├── core/              # Toolchain integration
│   ├── preprocessor/       # PDF data extraction
│   └── runtime/           # Visualization utilities
└── requirements.txt        # Python dependencies

Setup

Clone the Repository:
git clone <repository-url>
cd project_final


Create a Virtual Environment (recommended):
python -m venv cc_project
source cc_project/bin/activate  # On macOS/Linux
cc_project\Scripts\activate    # On Windows


Install Dependencies:
pip install -r requirements.txt

Required packages: ply, PyPDF2, reportlab, matplotlib, numpy, seaborn, scikit-learn.

Verify Test Case Files:Ensure the examples/ directory contains:

test_case_1.wiz to test_case_9.wiz
test_case_1_data.txt to test_case_9_data.txt



Generating PDFs
Test case data files (.txt) need to be converted to PDFs for preprocessing. Run:
cd scripts
python generate_test_pdfs.py

This generates test_case_1_data.pdf to test_case_9_data.pdf in examples/.
Running Test Cases
Individual Test Case
To run a specific test case (e.g., Test Case 2):
cd $PROJECT_ROOT
python scripts/run_toolchain.py examples/test_case_2_data.pdf examples/test_case_2.wiz


Output: 
outputs/output.py: Generated Python code.
outputs/histogram.png, outputs/scatter.png, outputs/plot.png (for visualization test cases).



All Test Cases
To run all test cases (1–9):
python scripts/run_all_tests.py


Output:
outputs/test_case_1_output.py to test_case_9_output.py
Visualization files (.png) for test cases with visualization primitives.



Visualization Outputs
Visualization outputs (e.g., histogram.png, scatter.png, plot.png) are saved in:
outputs/


Test Case 1: No visualizations (arithmetic only).
Test Case 2: histogram.png, scatter.png, plot.png.
Test Case 6: No visualizations (arithmetic only).
Test Case 7: histogram.png, plot.png.
Test Case 8: scatter.png.
Test Case 9: histogram.png, scatter.png, plot.png.