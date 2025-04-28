import re
import os
from collections import defaultdict
from .parser import parser, lexer, symbol_table, auxiliary_code_blocks

def compile_wizuall(wizuall_code, data_stream):
    symbol_table.clear()
    auxiliary_code_blocks.clear()
    
    wizuall_code = wizuall_code.strip()
    
    def process_data_stream(stream):
        temp_data = defaultdict(list)
        for line in stream.split('\n'):
            line = line.strip()
            if not line:
                continue
            try:
                parts = line.split(',', 1)
                if len(parts) == 2:
                    label = parts[0].strip()
                    if not re.match(r'^[a-zA-Z_][a-zA-Z_0-9]*$', label):
                        print(f"Warning: Invalid label: '{label}' - skipping")
                        continue
                    values = [float(x) for x in parts[1].split(',')]
                    temp_data[label].extend(values)
            except ValueError:
                print(f"Warning: Could not parse numeric values in line: '{line}'")
            except Exception as e:
                print(f"Error processing data line '{line}': {e}")
        return temp_data

    temp_data = process_data_stream(data_stream)
    data_assignments = []
    for label, values in temp_data.items():
        symbol_table[label] = values
        data_assignments.append(f"{label} = np.array({values})")  # Convert to NumPy array

    try:
        lexer.aux_code = []
        lexer.input(wizuall_code)
        lexer.lineno = 1
        parsed_program_lines = parser.parse(wizuall_code, lexer=lexer)
        if parsed_program_lines is None:
            print("Parsing failed. No Python code generated.")
            return None
    except SyntaxError as e:
        print(f"Compilation failed due to syntax error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error during parsing: {e}")
        return None

    def clean_code_lines(lines):
        cleaned = []
        for line in lines:
            if isinstance(line, str):
                if '\n' in line:
                    sublines = line.splitlines()
                    base_indent = None
                    for subline in sublines:
                        stripped = subline.strip()
                        if stripped:
                            if base_indent is None:
                                base_indent = len(subline) - len(subline.lstrip())
                            current_indent = len(subline) - len(subline.lstrip())
                            indent = max(0, current_indent - base_indent)
                            cleaned.append((' ' * indent) + stripped)
                else:
                    stripped = line.strip()
                    if stripped:
                        cleaned.append(stripped)
        return cleaned

    python_code = [
        "import matplotlib.pyplot as plt",
        "import numpy as np",
        "import seaborn as sns",
        "import math",
        "try:",
        "    from sklearn.cluster import KMeans",
        "except ImportError:",
        "    print('Warning: sklearn not installed, clustering functionality will not work')",
        "",
        f"OUTPUT_DIR = '{os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'outputs'))}'",
        "os.makedirs(OUTPUT_DIR, exist_ok=True)",
        ""
    ]

    if auxiliary_code_blocks:
        python_code.append("# --- Auxiliary Code ---")
        for block in auxiliary_code_blocks:
            lines = [line.strip() for line in block.splitlines() if line.strip()]
            python_code.extend(lines)
        python_code.append("# --- End Auxiliary Code ---")
        python_code.append("")

    if data_assignments:
        python_code.append("# --- Data Loading ---")
        python_code.extend(data_assignments)
        python_code.append("# --- End Data Loading ---")
        python_code.append("")

    if parsed_program_lines:
        python_code.append("# --- WizUALL Program ---")
        python_code.extend(clean_code_lines(parsed_program_lines))
        python_code.append("# --- End WizUALL Program ---")

    return '\n'.join(line.rstrip() for line in python_code if line is not None)