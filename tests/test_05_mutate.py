import unittest

from implementation.User import *
from implementation.program import *

class FiltrationTests(unittest.TestCase):
    def filtrationTests(self):
        userOne = User("1, , 18, a@a.no")
        self.assertTrue(filterUser(userOne, "2"))
