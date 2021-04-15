#!/bin/python3

import unittest
import filecmp


class HourglassSum(unittest.TestCase):

    def test_hourglass_sum_00(self):
            f_solution = open('data\\output\\output00.txt', 'r')
            solution = f_solution.read().replace("\n", "").replace("\r", "")
            f_solution.close()
            f_answer = open('output\\output00.txt', 'r')
            answer = f_answer.read().replace("\n", "").replace("\r", "")
            f_answer.close()
            self.assertEqual(solution, answer)

    def test_hourglass_sum_01(self):
            f_solution = open('data\\output\\output01.txt', 'r')
            solution = f_solution.read().replace("\n", "").replace("\r", "")
            f_solution.close()
            f_answer = open('output\\output01.txt', 'r')
            answer = f_answer.read().replace("\n", "").replace("\r", "")
            f_answer.close()
            self.assertEqual(solution, answer)

    def test_hourglass_sum_08(self):
            f_solution = open('data\\output\\output08.txt', 'r')
            solution = f_solution.read().replace("\n", "").replace("\r", "")
            f_solution.close()
            f_answer = open('output\\output08.txt', 'r')
            answer = f_answer.read().replace("\n", "").replace("\r", "")
            f_answer.close()
            self.assertEqual(solution, answer)

    
if __name__ == '__main__':
    unittest.main()