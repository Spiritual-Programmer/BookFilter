from dateutil import parser

authors = {
    "steven king": "Horror",
    "rudyard kipling": "Adventure",
    "isaac asimov": "Science Fiction",
    "suzanne collins": "YA Fiction"
}

class Book:
    def __init__(self, title, dateOfPublication, author, numberOfPages):
        self.title = title
        self.dateOfPublication = dateOfPublication
        self.numberOfPages = numberOfPages
        self.author = author

def getInput():
    splitInputByBook = []
    print("Enter books formatted as Title,Date,Author,Length with date formatted as mm/dd/yyyy or mm-dd-yyyy")
    while True:
        userInput = input()
        splitInputByBook.append(userInput)
        if userInput == "":
            splitInputByBook.pop()
            break
    return splitInputByBook

def parseInput(userInput):
    if userInput == None or len(userInput) == 0:
        raise ValueError("Invalid Input") from None
    else:
        booksArray = []
        for book in userInput:
            tempList = book.split(",")
            if len(tempList) == 4:
                booksArray.append(tempList)
        if len(booksArray) == 0:
            raise ValueError(
                "Invalid Input: Book must be formatted as title,date,author,length")
        booksArrayByDetails = []
        for book in booksArray:
            try:
                book[1] = parser.parse(book[1])
            except:
                raise ValueError(
                    "Date must be formatted in mm/dd/yyyy or mm-dd-yyyy") from None
            try:
                book[3] = int(book[3])
            except ValueError:
                raise ValueError(
                    "Invalid Input: Number of pages must be a valid number") from None
            booksArrayByDetails.append(
                Book(book[0], book[1], book[2].lower(), book[3]))
        return booksArrayByDetails

def findAuthorWithMostBooks(books):
    dictionary = {}
    for book in books:
        if book.author not in dictionary:
            dictionary[book.author] = 1
        else:
            dictionary[book.author] += 1
    maxNumberOfBooks = max(dictionary.values())
    mostBooksAuthorsList = []
    for author in dictionary:
        if dictionary[author] == maxNumberOfBooks:
            mostBooksAuthorsList.append(author)
    mostBooksAuthorObjects = []
    for author in mostBooksAuthorsList:
        for book in books:
            if book.author == author:
                mostBooksAuthorObjects.append(book)
    return mostBooksAuthorObjects

def findOldestBook(books):
    neededBook = books[0]
    oldestBook = parser.parse("12/31/2500")
    for book in books:
        currentDate = book.dateOfPublication
        if currentDate < oldestBook:
            oldestBook = currentDate
            neededBook = book
    return neededBook

def getGenre():
    try:
        genre = authors[neededBook.author]
    except KeyError as e:
        raise KeyError(
            f"Sorry but {e} is not in the given list of authors") from None

    print(f"{neededBook.title}, written by {genre} writer {neededBook.author.title()} on {neededBook.dateOfPublication} is {neededBook.numberOfPages} pages long")

#Calling Functions
splitInputByBook = getInput()
books = parseInput(splitInputByBook)
mostBooksAuthorObjects = findAuthorWithMostBooks(books)
neededBook = findOldestBook(mostBooksAuthorObjects)
getGenre()