from PyPDF2 import PdfFileReader
import re


def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        x = pdf.getXmpMetadata()
        print('font is : {}'.format(x.font))
        
        info = pdf.getDocumentInfo()
        num_of_pages = pdf.getNumPages()

    # print(info)


def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        
        # get the first page
        page = pdf.getPage(4793)
        print('Page Type : {} '.format(str(type(page))))

        text = page.extractText()
        print(text)


def text_search(path):
    print('text_search called')
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        String = '''ANCIENT INDIAN COMMERCE'''.upper()
        print('String after upper() is : {} '.format(String))

        for i in range(1, 100):
            PageObj = pdf.getPage(i)
            Text = PageObj.extractText()
            ReSearch = re.search(String, Text)
            if ReSearch is not None:
                print(ReSearch, "At Page No : {}".format(i))
                break
            
if __name__ == '__main__':
    path = 'books.pdf'
    # text_extractor(path)
    text_search(path)