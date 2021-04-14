import unittest
import filecmp


class CountingValleys(unittest.TestCase):

    def test_counting_valleys_00(self):
        f_solution = open('data\\output\\output00.txt', 'r')
        solution = f_solution.read().replace("\n", "").replace("\r", "")
        f_answer = open("output\\output00.txt", 'r')
        answer = f_answer.read().replace("\n", "").replace("\r", "")
        self.assertEqual(solution, answer)
        f_solution.close()
        f_answer.close()

    def test_counting_valleys_01(self):
        f_solution = open('data\\output\\output01.txt', 'r')
        solution = f_solution.read().replace("\n", "").replace("\r", "")
        f_answer = open("output\\output01.txt", 'r')
        answer = f_answer.read().replace("\n", "").replace("\r", "")
        self.assertEqual(solution, answer)
        f_solution.close()
        f_answer.close()


if __name__ == '__main__':
    unittest.main()
