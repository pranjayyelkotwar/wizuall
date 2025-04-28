import os
import sys
from ..preprocessor.extractor import extract_data
from ..compiler.codegen import compile_wizuall
from ..runtime.viz_utils import *

def run_toolchain(pdf_path, wizuall_path, output_path="output.py"):
    # Check if the PDF file exists
    if not os.path.exists(pdf_path):
        print(f"Error: {pdf_path} not found.")
        return 1

    # Extract data from the PDF
    print(f"Extracting data from {pdf_path}...")
    data_stream = extract_data(pdf_path)
    if not data_stream:
        print("Error: No data extracted from PDF. Exiting.")
        return 1
    print("Data extracted successfully.")

    # Read the WizUALL program
    try:
        with open(wizuall_path, 'r') as f:
            wizuall_code = f.read()
    except FileNotFoundError:
        print(f"Error: {wizuall_path} not found.")
        return 1

    # Compile the WizUALL code
    print("Compiling WizUALL code...")
    compiled_code = compile_wizuall(wizuall_code, data_stream)
    if compiled_code is None:
        print("Error: Compilation failed. No output generated.")
        return 1

    # Write the compiled Python code
    print(f"Writing compiled code to {output_path}...")
    with open(output_path, "w") as f:
        f.write(compiled_code)

    # Execute the compiled code
    print("Executing compiled code...")
    try:
        exec(open(output_path).read())
        print("Execution completed successfully.")
    except ImportError as e:
        print(f"Error: Missing dependency: {e}")
        print("Make sure all required packages are installed (numpy, matplotlib, seaborn, sklearn)")
        return 1
    except Exception as e:
        print(f"Error executing compiled code: {e}")
        return 1

    return 0

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python toolchain.py <pdf_path> <wizuall_path>")
        sys.exit(1)
    sys.exit(run_toolchain(sys.argv[1], sys.argv[2]))