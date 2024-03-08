 # PDF Merger

This Python script, `merge.py`, allows you to merge multiple PDF files into a single PDF document. It uses the PyMuPDF library to perform the merging operation.

## How to Use

1. **Install PyMuPDF**:
   - PyMuPDF is a third-party library that provides tools for working with PDF documents. To install it, run the following command in your terminal:
     ```
     pip install fitz
     ```

2. **Organize Your PDF Files**:
   - Place all the PDF files that you want to merge into a single folder on your computer.

3. **Run the Script**:
   - Open a terminal window and navigate to the directory where you saved the `merge.py` script.
   - Run the script by typing the following command, replacing `<input_folder>` with the actual path to the folder containing your PDF files:
     ```
     python merge.py <input_folder>
     ```

## Step-by-Step Explanation of the Code

### 1. Importing Libraries

```python
import os
import fitz  # PyMuPDF
```

- We start by importing the necessary libraries.
  - `os` is used for file and directory operations.
  - `fitz` is the PyMuPDF library that we'll use for merging PDF files.

### 2. Defining the `merge_pdfs` Function

```python
def merge_pdfs(input_path):
    output_path = os.path.join(input_path, "output.pdf")
    pdf_writer = fitz.open()

    for filename in os.listdir(input_path):
        if filename.endswith(".pdf"):
            with fitz.open(os.path.join(input_path, filename)) as pdf_reader:
                pdf_writer.insert_pdf(pdf_reader)

    pdf_writer.save(output_path)
    pdf_writer.close()
```

- The `merge_pdfs` function takes one argument, `input_path`, which is the path to the folder containing the PDF files to be merged.
- Inside the function:
  - We create an output path for the merged PDF file. It will be saved in the same folder as the input files, with the name "output.pdf".
  - We create a

<img src="https://img.shields.io/badge/PYTHON-black?style=for-the-badge&logo=python&logoColor=gold"/>
