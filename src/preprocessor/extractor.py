from collections import defaultdict
import PyPDF2

def extract_data(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            temp_data = defaultdict(list)
            for page in reader.pages:
                text = page.extract_text()
                if not text:
                    continue
                lines = text.split('\n')
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                    # Try comma-separated format (e.g., "x,1.0,2.0,3.0")
                    if ',' in line:
                        parts = line.split(',')
                        if len(parts) >= 2 and parts[0].isalpha():
                            label = parts[0].strip()
                            for value_str in parts[1:]:
                                value_str = value_str.strip()
                                if value_str:
                                    try:
                                        value = float(value_str)
                                        temp_data[label].append(value)
                                    except ValueError:
                                        print(f"Warning: Invalid numeric value '{value_str}' for label '{label}'")
                    # Try space-separated label-value pairs (e.g., "x 1.0 y 2.0")
                    else:
                        parts = line.split()
                        i = 0
                        while i < len(parts) - 1:
                            if parts[i].isalpha() and parts[i + 1].replace('.', '').replace('-', '').isdigit():
                                label = parts[i]
                                value_str = parts[i + 1]
                                try:
                                    value = float(value_str)
                                    temp_data[label].append(value)
                                except ValueError:
                                    print(f"Warning: Invalid numeric value '{value_str}' for label '{label}'")
                                i += 2
                            else:
                                i += 1
            if not temp_data:
                print("Warning: No valid data extracted from PDF")
                return ""
            data_stream = "\n".join(f"{label},{','.join(map(str, values))}" for label, values in temp_data.items())
            return data_stream
    except FileNotFoundError:
        print(f"Error: PDF file '{pdf_path}' not found")
        return ""
    except Exception as e:
        print(f"Error extracting data from PDF: {e}")
        return ""