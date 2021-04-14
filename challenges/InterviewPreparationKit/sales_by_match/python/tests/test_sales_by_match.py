import unittest
import filecmp


class SalesByMatch(unittest.TestCase):

    def test_sales_by_match_00(self):
            solution = "data\\output\\output00.txt"
            answer = "output\\output00.txt"
            self.assertTrue(filecmp.cmp(solution, answer, shallow=False))

    def test_sales_by_match_08(self):
            solution = "data\\output\\output08.txt"
            answer = "output\\output08.txt"
            self.assertTrue(filecmp.cmp(solution, answer, shallow=False))

    

if __name__ == '__main__':
    unittest.main()