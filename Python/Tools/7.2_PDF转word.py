import pdf2docx
from pdf2docx import Converter
pdf_file = "2.pdf"
docx_file= "2.docx"
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()