#https://pypdf2.readthedocs.io/en/3.x/
import PyPDF2
import os

merger = PyPDF2.PdfMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):        merger.append(file)
merger.write("combined.pdf")