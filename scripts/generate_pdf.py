from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

def generate_pdf_from_data(data_path, pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.drawString(100, 750, f"Data from {os.path.basename(data_path)}")
    y_position = 730
    with open(data_path, 'r') as f:
        for line in f:
            c.drawString(100, y_position, line.strip())
            y_position -= 20
    c.save()
    print(f"Generated {pdf_path}")

if __name__ == "__main__":
    examples_dir = "../examples"
    output_dir = examples_dir
    for i in range(1, 7):  # Updated to include test cases 1-6
        data_file = f"test_case_{i}_data.txt"
        pdf_file = f"test_case_{i}_data.pdf"
        data_path = os.path.join(examples_dir, data_file)
        pdf_path = os.path.join(output_dir, pdf_file)
        if os.path.exists(data_path):
            generate_pdf_from_data(data_path, pdf_path)
        else:
            print(f"Error: {data_path} not found")