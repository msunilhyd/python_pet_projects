from PyPDF2 import PdfFileReader
import re

def extract_books(path, list_of_books):
    books_dict = {}
    start_index_list = []
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        l = 4   
        for i in range(1, 53):
            String = list_of_books[i].strip()  
            #print('starting search for : {} from {}'.format(String, l)) 
            for j in range(l, 4794):
                # print('j is : {}'.format(j))
                PageObj = pdf.getPage(j)
                Text = PageObj.extractText()
                ReSearch = re.search(String, Text)
                if ReSearch is not None:
                    #print(ReSearch, "At Page No : {}".format(j))
                    #print('String is : {} '.format(String))
                    #print('Book Num is : {}'.format(i))
                    books_dict[String] = {'start' : j, 'end': 0}
                    start_index_list.append(j)
                    l = j
                    break
                # else:
                #     print(ReSearch, "Not found At Page No : {}".format(j))
                #     print('String is : {} '.format(String))
    #print('books_dict is : {}'.format(books_dict))
    start_index_list.append(0)
    k = 0
    for x in books_dict:
        r = str(x).replace("\n", "").replace("\\n", "")
        
        print(r)
        k=k+1
        for y in books_dict[x]:
            if y is 'end':
                #print(y, ':', books_dict[x][y])
                books_dict[x][y] = start_index_list[k] - 1  
            print(y, ':', books_dict[x][y])
                 
            

if __name__ == '__main__':
    path_txt_file = 'list_of_titles.txt'
    path_pdf_file = 'books.pdf'
    f = open(path_txt_file,'r')
    if f.mode == "r":
        contents = f.read()
        list_of_books = contents.split(';')
        # print('list_of_books is : {}'.format(list_of_books))
        extract_books(path_pdf_file, list_of_books)
