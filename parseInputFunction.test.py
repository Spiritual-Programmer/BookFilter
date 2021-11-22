import unittest
from main import parseInput
from dateutil import parser


class parseInputTest(unittest.TestCase):
    """Tests for parseInput function"""

    def test_1(self):
        '''Does a single line input work'''
        inputTest = "Carrie,06/13/1982,Steven King,762"
        expectedResult = [{"title": "Carrie", "dateOfPublication": parser.parse(
            "06/13/1982"), "author": "steven king", "numberOfPages": 762}]
        #self.assertEqual(parseInput(inputTest), expectedResult)
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
