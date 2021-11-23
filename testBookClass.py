import unittest
from main import Book

class TestBookClass(unittest.TestCase):
    """Tests for the Book Class"""

    def test_store_responses(self):
        '''Given books, does it store correctly'''
        inputTest = Book("Carrie","06/13/1982","Steven King","762")

        self.assertIn('Carrie', inputTest.title)
        self.assertIn('06/13/1982', inputTest.dateOfPublication)
        self.assertIn('Steven King', inputTest.author)
        self.assertIn("762", inputTest.numberOfPages)


if __name__ == '__main__':
    unittest.main()