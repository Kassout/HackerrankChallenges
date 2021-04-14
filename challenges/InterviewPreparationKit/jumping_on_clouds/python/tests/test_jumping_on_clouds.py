#!/bin/python3

import unittest
import filecmp


class JumpingOnClouds(unittest.TestCase):

    def test_jumping_on_clouds_00(self):
            f_solution = open('data\\output\\output00.txt', 'r')
            solution = f_solution.read().replace("\n", "").replace("\r", "")
            f_solution.close()
            f_answer = open('output\\output00.txt', 'r')
            answer = f_answer.read().replace("\n", "").replace("\r", "")
            f_answer.close()
            self.assertEqual(solution, answer)

    def test_jumping_on_clouds_01(self):
            f_solution = open('data\\output\\output01.txt', 'r')
            solution = f_solution.read().replace("\n", "").replace("\r", "")
            f_solution.close()
            f_answer = open('output\\output01.txt', 'r')
            answer = f_answer.read().replace("\n", "").replace("\r", "")
            f_answer.close()
            self.assertEqual(solution, answer)
            f_solution.close()
            f_answer.close()

    
if __name__ == '__main__':
    unittest.main()