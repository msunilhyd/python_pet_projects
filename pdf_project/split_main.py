import PyPDF2
import os

def PDFsplit(pdf, splits, title):
        # creating input pdf file object
        pdfFileObj = open(pdf, 'rb')
        
        # creating the pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # starting index of the first slice
        start = splits[0]

        # starting index of the last slice
        end = splits[1]

        print('Title is : {}, start : {}, end : {}'.format(title, start, end))
        
        pdfWriter = PyPDF2.PdfFileWriter()

        # output pdf file name
        outputpdf = title.replace('_','') + '.pdf'

        # adding pages to pdf pdfWriter object
        for page in range(start,end+1):
                pdfWriter.addPage(pdfReader.getPage(page))

        # writing split pdf pages to pdf file
        with open(outputpdf, "wb") as f:
                pdfWriter.write(f)
                os.rename('./'+outputpdf, 'final_books/' + outputpdf)

        # # interchanging page split start position to the next split
        # start = end

        # try:
        #         # setting split end position for next split
        #         end = splits[i+1]
        # except IndexError:
        #         # setting split end position for last split
        #         end = pdfReader.numPages

        # closing the input pdf file object
        pdfFileObj.close()

class Book:
        def __init__(self, title, start, end):
                self.title = title
                self.start = start
                self.end = end

        def __repr__(self):
                return "Book : {}; start : {}; end : {}".format(self.title, self.start, self.end)

book_list = []

def main():
    # open the file and read the contents
    f = open('books_info.txt','r')
    if f.mode == 'r':
        contents = f.readlines()
        print('size of contents is : {}'.format(len(contents)))
        
        for i in range(0, 148, 3):
                print('i is : {}'.format(i))
                print('contents[{}] is = {}'.format(i, contents[i]))
                book = Book(contents[i].strip(), contents[i+1].strip(), contents[i+2].strip())
                book_list.append(book) 

        print('length of book_list is : {}'.format(len(book_list)))
        print('book_list is : {}'.format(book_list))


def split_pdf():

        # pdf file to split
        pdf = 'books.pdf'
        for book in book_list:
                splits = []
                # split page positions
                splits.append(int(book.start))
                splits.append(int(book.end))
                # calling PDFsplit function to split pdf
                PDFsplit(pdf,splits, book.title)

        print('printing book_list length : {}'.format(len(book_list)))



if __name__ == "__main__":
        book1 = Book('First Book by Sunil', 0, 10)
        # print(book1)
        main()
        split_pdf()