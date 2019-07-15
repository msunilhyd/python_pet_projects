class Book:
        def __init__(self, title, start, end):
                self.title = title
                self.start = start
                self.end = end

        def __repr__(self):
                return "Book : {}, start : {}, end : {}".format(self.title, self.start, self.end)



def main():
    # open the file and read the contents
    book_list = []
    f = open('books_info.txt','r')
    if f.mode == 'r':
        contents = f.readlines()
        print('size of contents is : {}'.format(len(contents)))
        
        for i in range(0, 9, 3):
                print('i is : {}'.format(i))
                print('contents[{}] is = {}'.format(i, contents[i]))
                book = Book(contents[i], contents[i+1], contents[i+2])
                book_list.append(book) 

        print('length of book_list is : {}'.format(len(book_list)))

if __name__ == "__main__":
        book1 = Book('First Book by Sunil', 0, 10)
        # print(book1)
        main()
