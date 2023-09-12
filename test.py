import time
import allure
import pytest
import unittest

class Demo(unittest.TestCase):
    @staticmethod
    def test_1():
        expected = 5
        actual = 5
        assert actual == expected

