import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.core.toolchain import run_toolchain

def ensure_output_directory_exists(output_dir):
    """Ensure the outputs directory exists."""
    os.makedirs(output_dir, exist_ok=True)

def main():
    if len(sys.argv) != 3:
        print("Usage: python run_toolchain.py <pdf_path> <wizuall_path>")
        sys.exit(1)

    # Define output directory and ensure it exists
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'outputs')
    ensure_output_directory_exists(output_dir)

    # Set output path to outputs directory
    output_path = os.path.join(output_dir, 'output.py')

    # Run the toolchain
    sys.exit(run_toolchain(sys.argv[1], sys.argv[2], output_path))

if __name__ == "__main__":
    main()