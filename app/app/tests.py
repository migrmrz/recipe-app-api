from django.test import TestCase
from app.calc import sum


class CalcTest(TestCase):

    def test_add_numers(self):
        """Test that adds two numbers"""
        self.assertEqual(sum(3, 8), 11)
