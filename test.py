import time
import allure
import pytest
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Demo(unittest.TestCase):
    @staticmethod
    def test_1():
        expected = 5
        actual = 5
        assert actual == expected, 'not correct'

    @staticmethod
    def test_2():
        driver = webdriver.Chrome()
        driver.get('https://www.google.com')
        time.sleep(2)
        title = driver.title
        assert title == 'Googl'
        #driver.find_element(By.CSS_SELECTOR, selector).click()


