import unittest

##   unit tests for creating a multiplication table
##   for helping a grader schooler learn their times tables.
##
##   Example of what we want to make:
##
##   makeMultTable(4,3)
##
##   means 4 rows and 3 columns up to 12
##   More the point: the number of rows and columns should
##   fit into 1 or 2 digits, and the product should fit in 3 digits.
##
##   e.g.
##
##   | 1 | 2 | 3 |
##---+---+---+---+
## 1 |  1|  2|  3|
##---+---+---+---+
## 2 |  2|  4|  6| 
##---+---+---+---+
## 3 |  3|  6|  9|
##---+---+---+---+
## 4 |  4|  8| 15| 
##---+---+---+---+
##
##   makeMultTable(3,1)
##
##
##   | 1 |
##---+---+
## 1 |  1|
##---+---+
## 2 |  2|  
##---+---+
## 3 |  3| 
##---+---+
##


import MultTables

class MultTableTest(unittest.TestCase):

    def test_separator_row_3_columns(self):
        expected="---+---+---+---+"
        actual=MultTables.separator_row(3);
        self.assertEqual(actual,expected)

    def test_separator_row_1_column(self):
        expected="---+---+"
        actual=MultTables.separator_row(1);
        self.assertEqual(actual,expected)

    def test_header_row_1_columns(self):
        self.assertEqual(MultTables.header_row(1),"   | 1 |")
 
    def test_header_row_3_columns(self):
        self.assertEqual(MultTables.header_row(3),"   | 1 | 2 | 3 |")

if __name__ == "__main__":
  unittest.main()















     
