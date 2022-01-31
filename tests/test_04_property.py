from hypothesis import given
from hypothesis.strategies import text, lists
import unittest
from implementation.program import distinctList


class TestDistinct(unittest.TestCase):
    @given(lists(text()))
    def test_distinct(self, elements):
        dist = distinctList(elements)
        self.assertGreaterEqual(len(elements), len(dist))