from PyPDF2 import PdfFileReader
import re

def extract_books(path, list_of_books):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        for i in range(1, 3):
            String = list_of_books[i]            
            for j in range(1, 100):
                # print('j is : {}'.format(j))
                PageObj = pdf.getPage(j)
                Text = PageObj.extractText()
                ReSearch = re.search(String.strip(), Text)
                if ReSearch is not None:
                    print(ReSearch, "At Page No : {}".format(j))
                    print('String is : {} '.format(String))
                    break
                else:
                    print(ReSearch, "Not found At Page No : {}".format(j))
                    print('String is : {} '.format(String))
                    

if __name__ == '__main__':
    path_txt_file = 'list_of_titles.txt'
    path_pdf_file = 'books.pdf'
    f = open(path_txt_file,'r')
    if f.mode == "r":
        contents = f.read()
        list_of_books = contents.split(';')
        # print('list_of_books is : {}'.format(list_of_books))
        extract_books(path_pdf_file, list_of_books)
