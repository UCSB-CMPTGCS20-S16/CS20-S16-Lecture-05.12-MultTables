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
## 4 |  4|  8| 12| 
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

    def test_table_row_row_2_with_3_columns(self):
        expected = " 2 |  2|  4|  6|"
        actual = MultTables.table_row(2,3)
        self.assertEqual(actual,expected)
 
    def test_table_row_row_3_with_3_columns(self):
        expected = " 3 |  3|  6|  9|"
        actual = MultTables.table_row(3,3)
        self.assertEqual(actual,expected)

    def test_table_row_row_4_with_3_columns(self):
        expected = " 4 |  4|  8| 12|"
        actual = MultTables.table_row(4,3)
        self.assertEqual(actual,expected)
 

    def test_mult_table_4_rows_3_columns(self):
        expected = '''   | 1 | 2 | 3 |
---+---+---+---+
 1 |  1|  2|  3|
---+---+---+---+
 2 |  2|  4|  6|
---+---+---+---+
 3 |  3|  6|  9|
---+---+---+---+
 4 |  4|  8| 12|
---+---+---+---+
'''
        actual = MultTables.mult_table(4,3)
        self.assertEqual(actual,expected)

    def test_mult_table_2_rows_2_columns(self):
        expected = '''   | 1 | 2 |
---+---+---+
 1 |  1|  2|
---+---+---+
 2 |  2|  4|
---+---+---+
'''
        actual = MultTables.mult_table(2,2)
        self.assertEqual(actual,expected)

        


if __name__ == "__main__":
  unittest.main()















     
