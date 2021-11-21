authors = [
    {
        "name": "steven king",
        "genre": "Horror"
    },
    {
        "name": "rudyard kipling",
        "genre": "Adventure"
    },
    {
        "name": "issac asimov",
        "genre": "Science Fiction"
    },
    {
        "name": "suzanne collins",
        "genre": "YA Fiction"
    }
]


class Book:
    def __init__(self, title, dateOfPublication, author, numberOfPages):
        self.title = title
        self.dateOfPublication = dateOfPublication
        self.numberOfPages = numberOfPages
        self.author = author

    def getObjects(self):
        bookObject = {
            "title": self.title,
            "dateOfPublication": self.dateOfPublication,
            "author": self.author,
            "numberOfPages": self.numberOfPages
        }
        return bookObject


splitInputByBook = []
print("Enter books formatted as Title,Date,Author,Length with date formatted as mm/dd/yyyy")
while True:
    userInput = input()
    splitInputByBook.append(userInput)
    if userInput == "":
        splitInputByBook.pop()
        break
print("ser input:", splitInputByBook)


def getbookArrayByDetails(book):
    return Book(book[0], book[1], book[2], book[3])


bookclass = (getbookArrayByDetails(["title", "date", "pages", "author"]))
print(bookclass.getObjects())


def parseInput(userInput):
    if userInput == None or len(userInput) == 0:
        raise ValueError("Invalid Input")
    else:
        #booksArray = filter(lambda book: book.split(","),splitInputByBook)
        booksArray = []
        for book in userInput:
            booksArray.append(book.split(","))
        print("booksarray:", list(booksArray))
        booksArrayByDetails = map(getbookArrayByDetails, booksArray)
        print(booksArrayByDetails)


parseInput(splitInputByBook)
