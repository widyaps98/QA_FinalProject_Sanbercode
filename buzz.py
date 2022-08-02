from lib2to3.pgen2 import driver
import unittest
import time
import random
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select 

class TestingOrangeHrm(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install()) 

    def tc_edit_contact_detail_success(self): 
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
        browser.find_element(By.ID,"menu_buzz_viewBuzz").click() # klik menu Buzz
        time.sleep(1)
        browser.find_element(By.ID,"images-tab-label").click() # klik menu Contact Details
        time.sleep(1)

        # step upload foto
        browser.find_element(By.ID,"image-upload-button").send_keys("D:/PROJECT_QA/Katalon.png") #Klik button Edit
        time.sleep(1)
        browser.find_element(By.ID,"imageUploadBtn").click() #Klik button Edit
        time.sleep(1)

        #validasi
        browser.find_element(By.ID,"postBody").is_displayed()
        time.sleep(1)

    def tearDown(self): 
        self.browser.close() 


if __name__ == "__main__": 
    unittest.main()