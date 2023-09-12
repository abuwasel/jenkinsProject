import time
import allure
import pytest

class Demo:
    @staticmethod
    def test_1():
        print("Hello object world!")

demo = Demo()
demo.test_1()
