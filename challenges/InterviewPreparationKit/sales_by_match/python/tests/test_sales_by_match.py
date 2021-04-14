import unittest
import filecmp


class SalesByMatch(unittest.TestCase):

    def test_sales_by_match_00(self):
        f_solution = open('data\\output\\output00.txt', 'r')
        solution = f_solution.read().replace("\n", "").replace("\r", "")
        f_answer = open("output\\output00.txt", 'r')
        answer = f_answer.read().replace("\n", "").replace("\r", "")
        self.assertEqual(solution, answer)
        f_solution.close()
        f_answer.close()

    def test_sales_by_match_08(self):
        f_solution = open('data\\output\\output08.txt', 'r')
        solution = f_solution.read().replace("\n", "").replace("\r", "")
        f_answer = open("output\\output08.txt", 'r')
        answer = f_answer.read().replace("\n", "").replace("\r", "")
        self.assertEqual(solution, answer)
        f_solution.close()
        f_answer.close()


if __name__ == '__main__':
    unittest.main()