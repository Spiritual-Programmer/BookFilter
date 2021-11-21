from dateutil import parser

authors = {
    "steven king": "Horror",
    "rudyard kipling": "Adventure",
    "issac asimov": "Science Fiction",
    "suzanne collins": "YA Fiction"
}


class Book:
    def __init__(self, title, dateOfPublication, author, numberOfPages):
        self.title = title
        self.dateOfPublication = dateOfPublication
        self.numberOfPages = numberOfPages
        self.author = author


splitInputByBook = []
print("Enter books formatted as Title,Date,Author,Length with date formatted as mm/dd/yyyy")
while True:
    userInput = input()
    splitInputByBook.append(userInput)
    if userInput == "":
        splitInputByBook.pop()
        break
print("User input:", splitInputByBook)


def parseInput(userInput):
    if userInput == None or len(userInput) == 0:
        raise ValueError("Invalid Input")
    else:
        #booksArray = filter(lambda book: book.split(","),splitInputByBook)
        booksArray = []
        for book in userInput:
            tempList = book.split(",")
            if len(tempList) == 4:
                booksArray.append(tempList)
        if len(booksArray) == 0:
            raise ValueError("Invalid Input")
        booksArrayByDetails = []
        for book in booksArray:
            booksArrayByDetails.append(
                Book(book[0], book[1], book[2], book[3]))
        return booksArrayByDetails


books = parseInput(splitInputByBook)
print(books)


def findAuthorWithMostBooks(books):
    dictionary = {}
    for book in books:
        if book.author not in dictionary:
            dictionary[book.author] = 1
        else:
            dictionary[book.author] += 1
    maxNumberOfBooks = max(dictionary.values())
    for author in dictionary:
        if dictionary[author] == maxNumberOfBooks:
            return author


mostBooksAuthor = findAuthorWithMostBooks(books)
print(mostBooksAuthor, "type:", type(mostBooksAuthor))


def findOldestBook(books):
    neededBook = books[0]
    oldestBook = parser.parse("12/31/2500")
    for book in books:
        currentDate = parser.parse(book.dateOfPublication)
        if currentDate < oldestBook:
            oldestBook = currentDate
            neededBook = book
    return neededBook


neededBook = findOldestBook(books)

genre = authors[mostBooksAuthor.lower()]

print(f"{neededBook.title}, written by {genre} writer {neededBook.author} on {neededBook.dateOfPublication} is {neededBook.numberOfPages} pages long")
