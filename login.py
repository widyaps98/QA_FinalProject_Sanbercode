import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestingOrangeHrm(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def Org_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik button login
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"welcome").text
        self.assertIn('Welcome', response_data)

    def Org_failed_login_with_empty_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # kosongkan password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik button login
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.ID,"spanMessage").text
        self.assertEqual(response_message, 'Username cannot be empty')

    def Org_failed_login_wrong_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs OrangeHrm
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("zzzzzzz") #isi password salah
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik button login
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.ID,"spanMessage").text
        self.assertEqual(response_message, 'Invalid credentials')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()