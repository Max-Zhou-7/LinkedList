from Book import *
from BookCollectionNode import *

class BookCollection:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def getNumberOfBooks(self):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.getNext()
        return count

    def insertBook(self, book):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > book:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = BookCollectionNode(book)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def getBooksByAuthor(self,author):
        current = self.head
        output = ""
        while current != None:
            if current.getData().getAuthor().casefold() == author.casefold():
                output += current.getData().getBookDetails() + "\n"
            current = current.getNext()
        return output

    def getAllBooksInCollection(self):
        current = self.head
        output = ''
        while current != None:
            output += current.getData().getBookDetails() + "\n"
            current = current.getNext()
        return output
        
    def removeAuthor(self,author):
        current = self.head
		
        if current == None:
            return
        previous = None
        found = False
        while not found: 
            if current == None:
                return
            if current.getData().getAuthor().casefold() == author.casefold():
                found = True
            else:
                previous = current
                current = current.getNext()

        while current != None and current.getData().getAuthor().casefold() == author.casefold():
            current = current.getNext()
        if found == True and previous == None:
            self.head = current
		
        if found == True and previous != None:
            previous.setNext(current)

    def recursiveSearchTitle(self,title, bookNode):
        if bookNode == None:
            return False
        if bookNode.getData().getTitle().casefold() == title.casefold():
            return True
        else:
            
            return self.recursiveSearchTitle(title,bookNode.getNext())


# b0 = Book("Cujo", "King, Stephen", 1981)
# b1 = Book("The Shining", "King, Stephen", 1977)
# b2 = Book("Ready Player One", "Cline, Ernest", 2011)
# b3 = Book("Rage", "King, Stephen", 1977)

# bc = BookCollection()
# bc.insertBook(b0)
# bc.insertBook(b1)
# bc.insertBook(b2)
# bc.insertBook(b3)
# # print(bc.getBooksByAuthor("Cline, eRNest"))
# # bc.removeAuthor("Cline, Ernest")
# print(bc.getAllBooksInCollection())
# # bc.removeAuthor("Cline, ErnesT")
# # print(bc.getAllBooksInCollection())
# bc.removeAuthor("King, stephen")
# print(f"{bc.getNumberOfBooks()}")
# print(bc.getAllBooksInCollection())
# # bc.insertBook(b2)
# # print(bc.getAllBooksInCollection())
# # b0 = Book("Cujo", "King, Stephen", 1981)
# # b1 = Book("The Shining", "King, Stephen", 1977)
# # bc.insertBook(b0)
# # bc.insertBook(b1)
# # assert bc.recursiveSearchTitle("CUJO", bc.head) == True
# # assert bc.recursiveSearchTitle("Twilight", bc.head) == False
