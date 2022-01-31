import unittest

from implementation.User import *
from implementation.Database import *
from implementation.program import *

class UnitTests(unittest.TestCase):
    def testOk(self):
        userOne = User("1, , 20, a@a.no")
        userTwo = User("2, 1, 32, builder@bob.no")
        class TestDatabase(Database):
            def findAd(self, adId: int) -> Ad:
                return Ad("3, 15, 1")
            def usersWithAdAsFavourite(self, adId: int) -> list[User]:
                return [userOne, userTwo]
        result = program(TestDatabase(), "1_1")
        self.assertEqual(result, "Favourited by: builder@bob.no")