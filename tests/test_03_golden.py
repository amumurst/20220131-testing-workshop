from distutils.file_util import write_file
import unittest

from implementation.program import program
from implementation.Database import CSVDatabase

class IntegrationTests(unittest.TestCase):
    def goldenTest(self, number):
        adFile = "tests/test_03_golden/" + number + "_ads.txt"
        userFile = "tests/test_03_golden/" + number + "_users.txt"
        outputFile = "tests/test_03_golden/" + number + "_output.txt"
        inputFile = "tests/test_03_golden/" + number + "_input.txt"
        with open(inputFile) as input:
            with open(outputFile) as output:
                result = program(CSVDatabase(userFile, adFile), input.read())
                self.assertEqual(result, output.read())

    def testOk(self):
        self.goldenTest("01")
