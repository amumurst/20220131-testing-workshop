import unittest
import uuid
import os

from implementation.Database import CSVDatabase
from implementation.program import *

class IntegrationTests(unittest.TestCase):
    def writeFile(self, content: str) -> str:
        filename = str(uuid.uuid4()) + ".txt"
        file = open(filename, "a")
        file.write(content)
        file.close()
        return filename
    def deleteFile(self, filename: str):
        os.remove(filename)

    def testOk(self):
        users = """1, 1, 32, builder@bob.no
2, , 100, donald@duck.com"""
        ads = """1, 200000, 1
2, 4900000, 3"""
        
        userFile = self.writeFile(users)
        adsFile = self.writeFile(ads)

        result = program(CSVDatabase(userFile, adsFile), "1_1")

        self.deleteFile(userFile)
        self.deleteFile(adsFile)
        
        self.assertEqual(result, "your ad seems to need some love")