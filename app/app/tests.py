from django.test import TestCase
# from app.app.calc import add
from .calc import add


class CalcTests(TestCase):
    def test_add_numbers(self):
        """ Text that two numbers are added together """
        self.assertEquals(add(3, 8), 11)

    def test_subtract_numbers(self):
        """ Text that two numbers are added together """
        self.assertEquals(add(5, 11), 6)

