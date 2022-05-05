from BookCollectionNode import *
from BookCollection import *
from Book import *
bc = BookCollection()
bcn = BookCollectionNode(Book)
b0 = Book("Cujo", "King, Stephen", 1981)
b1 = Book("The Shining", "King, Stephen", 1977)
b2 = Book("Ready Player One", "Cline, Ernest", 2011)
b3 = Book("Rage", "King, Stephen", 1977)
def test_Book():

    assert b2.getBookDetails() == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011"
    assert (b2 > b0) == False
    assert b0.getYear() == 1981
    assert b2.getTitle() == "Ready Player One"

def test_BookCollectionNode():
    bcn.setData(b2)
    bcn.setNext(b0)

    assert bcn.getData().getBookDetails() == "Title: Ready Player One, \
Author: Cline, Ernest, Year: 2011"
    

def test_getBooksByAuthor():

    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3) 
    #print(bc.getBooksByAuthor("KiNg, stEPHEn"))  
    assert bc.getBooksByAuthor("KiNg, stEPHEn") == "Title: Rage, Author: King, Stephen, Year: 1977\
\nTitle: The Shining, Author: King, Stephen, Year: 1977\
\nTitle: Cujo, Author: King, Stephen, Year: 1981\n"
    assert bc.getBooksByAuthor("CLINE, ERNEST") == "Title: Ready Player One, \
Author: Cline, Ernest, Year: 2011\n"

def test_getNumberOfBooks():
    assert bc.getNumberOfBooks() == 4

def test_getAllBooks():
    assert bc.getAllBooksInCollection()== "Title: Ready Player One, Author: Cline, Ernest, Year: 2011\
\nTitle: Rage, Author: King, Stephen, Year: 1977\nTitle: The Shining, Author: King, Stephen, Year: 1977\nTitle: Cujo, Author: King, Stephen, Year: 1981\n"

def test_removeAuthor():
    bc.removeAuthor("CLINE, ernest")
    assert bc.getBooksByAuthor("KiNg, stEPHEn") == "Title: Rage, \
Author: King, Stephen, Year: 1977\nTitle: The Shining, \
Author: King, Stephen, Year: 1977\nTitle: Cujo, \
Author: King, Stephen, Year: 1981\n"
    bc.removeAuthor("kINg, sTEPhen")
    assert bc.getBooksByAuthor("CLINE, ernest") == ""

def test_recursive():
    bc.insertBook(b0)
    bc.insertBook(b1)
    assert bc.recursiveSearchTitle("CUJO", bc.head) == True
    assert bc.recursiveSearchTitle("Twilight", bc.head) == False