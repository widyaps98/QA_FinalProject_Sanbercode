from lib2to3.pgen2 import driver
import unittest
import time
import random
from xmlrpc.client import Boolean
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select 

class TestingOrangeHrm(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install()) 

    def test_import_data(self): 
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
        browser.find_element(By.ID,"menu_pim_viewPimModule").click() # klik menu PIM
        time.sleep(1)
        browser.find_element(By.ID,"menu_pim_Configuration").click() # klik menu Configuration
        time.sleep(1)
        browser.find_element(By.ID,"menu_admin_pimCsvImport").click() # klik Menu Data Import
        time.sleep(1)

        #step_input_data
        browser.find_element(By.ID,"pimCsvImport_csvFile").send_keys("D:/PROJECT_QA/importData.csv") # Upload Data
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click() # klik Button Save
        time.sleep(1)

    def test_import_data_failed(self): 
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
        browser.find_element(By.ID,"menu_pim_viewPimModule").click() # klik menu Pim
        time.sleep(1)
        browser.find_element(By.ID,"menu_pim_Configuration").click() # klik menu Configuration
        time.sleep(1)
        browser.find_element(By.ID,"menu_admin_pimCsvImport").click() # klik Menu Data Import
        time.sleep(1)

        #step_input_data
        browser.find_element(By.ID,"pimCsvImport_csvFile").send_keys("D:/PROJECT_QA/Katalon.png") # Upload File 
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click() # klik Button Save
        time.sleep(1)

        #valisadi
        response_message = browser.find_element(By.CLASS_NAME,"fadable").text 
        self.assertEqual(response_message, 'Failed to Import: File Type Not Allowed')

    def test_button_upload_without_file(self): 
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
        browser.find_element(By.ID,"menu_pim_viewPimModule").click() # klik menu Pim
        time.sleep(1)
        browser.find_element(By.ID,"menu_pim_Configuration").click() # klik menu Configuration
        time.sleep(1)
        browser.find_element(By.ID,"menu_admin_pimCsvImport").click() # klik menu Import Data
        time.sleep(1)

        #step_input_data
        browser.find_element(By.ID,"btnSave").click() # klik Button Save
        time.sleep(1)

        #valisadi
        Boolean 
        result = browser.find_element(By.XPATH,("//*[@id='frmPimCsvImport']/fieldset/ol[1]/li/span[text()='Required']")).is_displayed() #validasi erorr message ditampilkan


    def tearDown(self): 
        self.browser.close() 


if __name__ == "__main__": 
    unittest.main()