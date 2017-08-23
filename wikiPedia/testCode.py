from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains

class TestAddition(unittest.TestCase):
    def setUp(self):
        print("Setting up the test")

    def tearDown(self):
        print("Tearing down the test")

    def test_twoPlusTwo(self):
        total=2+2
        self.assertEqual(4,total)

class TestWikipedia(unittest.TestCase):
    bsObj=None
    @classmethod
    def setUpClass(cls):
        global bsObj
        url="http://en.wikipedia.org/wiki/Monty_Python"
        bsObj=BeautifulSoup(urlopen(url))

    def test_titleText(self):
        global bsObj
        pageTitle=bsObj.find("h1").get_text()
        self.assertEqual("Monty Python",pageTitle)

    def test_contentExists(self):
        global bsObj
        content=bsObj.find("div",{"id":"mw-content-text"})
        self.assertIsNone(content)

class TestDrag(unittest.TestCase):
    driver=None
    def setUp(self):
        global driver
        driver=webdriver.PhantomJS(executable_path="phantomjs")
        url='http://pythonscraping.com/pages/javascript/draggableDemo.html'
        driver.get(url)

    def tearDown(self):
        print("Tearing down the test")

    def test_drag(self):
        global driver
        element=driver.find_element_by_id("draggable")
        target=driver.find_element_by_id("div2")
        actions=ActionChains(driver)
        actions.drag_and_drop(element,target).perform()

        self.assertEqual("You are definitely not a bot!",driver.find_element_by_id("message").text)


if __name__=='__main__':
    unittest.main()