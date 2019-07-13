import PyPDF2

object = open('books.pdf', 'rb')
reader = PyPDF2.PdfFileReader(object)

print(reader.numPages)