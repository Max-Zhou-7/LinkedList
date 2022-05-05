class Book:
    def __init__(self, title = "", author = "", year = None):
        self.title = title
        self.author = author
        self.year = year
    
    def getTitle(self):
        return self.title
    def getAuthor(self):
        return self.author
    def getYear(self):
        return self.year
    def getBookDetails(self):
        return "Title: {}, Author: {}, Year: {}"\
            .format(self.title,self.author,self.year)
    def __gt__(self,rhs):
        if self.author > rhs.author:
            return True
        elif self.author == rhs.author:
            if self.year > rhs.year:
                return True
            elif self.year == rhs.year:
                return self.title > rhs.title

            else:
                return False
        else:
            return False

                


    
# b = Book("Ready Player One", "Cline, Ernest", 2011)
# b0 = Book("Cujo", "King, Stephen", 1981)
# # print(b.getBookDetails())
# assert b0>b == True
