import os
import fitz  # PyMuPDF

def merge_pdfs(input_path):
    output_path = os.path.join(input_path, "output.pdf")
    pdf_writer = fitz.open()

    for filename in os.listdir(input_path):
        if filename.endswith(".pdf"):
            with fitz.open(os.path.join(input_path, filename)) as pdf_reader:
                pdf_writer.insert_pdf(pdf_reader)

    pdf_writer.save(output_path)
    pdf_writer.close()

if __name__ == "__main__":
    input_folder = input("Enter the folder path containing PDF files: ")

    if os.path.exists(input_folder):
        merge_pdfs(input_folder)
        print("PDF files merged successfully.")
    else:
        print("Invalid folder path. Please provide a valid path.")
