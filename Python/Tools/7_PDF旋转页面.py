import PyPDF2

# Open the existing PDF file
minutesFile = open('1759F5-China.pdf', 'rb')

# Read the PDF file
Reader = PyPDF2.PdfReader(minutesFile)

# Get the first page
page = Reader.pages[0]

# Rotate the page 90 degrees clockwise
page.rotate(90)

# Create a PDF writer object
pdfWriter = PyPDF2.PdfWriter()

# Add the rotated page to the writer
pdfWriter.add_page(page)

# Write the rotated page to a new PDF file
resultPdfFile = open('1759F5-China.pdf', 'wb')
pdfWriter.write(resultPdfFile)

# Close all files
resultPdfFile.close()
minutesFile.close()