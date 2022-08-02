from lib2to3.pgen2 import driver
from tkinter.tix import Select 
import unittest
import time
import random
from xmlrpc.client import boolean
from selenium import webdriver
import selenium 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select 

class TestingOrangeHrm(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install()) 

    def test_search_user_role(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)

        # step login
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik button login
        time.sleep(1)

        # step pilih menu
        browser.find_element(By.XPATH,"//*[@id='content']/div").is_displayed() # klik menu Dashboard
        time.sleep(1)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()