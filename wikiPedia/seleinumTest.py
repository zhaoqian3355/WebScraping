from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.PhantomJS("/Users/zhaoqian/Documents/webDriver/chromedriver")
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html") 
try:
    element=WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"loadedButton")))

    element.click()
finally:
    print(driver.find_element_by_id("content").text)
    driver.close()