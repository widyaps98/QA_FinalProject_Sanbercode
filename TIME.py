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
        browser.find_element(By.ID,"menu_time_viewTimeModule").click() # klik menu My Info
        time.sleep(1)
        browser.find_element(By.ID,"menu_time_viewTimeModule").click() # klik menu Contact Details
        time.sleep(1)
        browser.find_element(By.ID,"menu_time_viewEmployeeTimesheet").click() # klik menu Contact Details
        time.sleep(1)

        # step update data
        browser.find_element(By.ID,"//*[@id='employee/]").send_keys("Charlie Carter") #Klik button View
        time.sleep(1)
        edit = browser.find_element(By.ID,"btnView").click 
        time.sleep(1)

        #validastion
        response_message = browser.find_element(By.ID,"timesheet").is_displayed()

    def tearDown(self): 
        self.browser.close() 


if __name__ == "__main__": 
    unittest.main()