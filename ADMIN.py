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
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a/b").click() # klik menu admin
        time.sleep(1)
        browser.find_element(By.ID,"menu_admin_UserManagement").click() # klik menu User Management
        time.sleep(1)
        browser.find_element(By.ID,"menu_admin_viewSystemUsers").click() # klik Users
        time.sleep(1)

        # step create job title
        pilih = Select(browser.find_element(By.ID,"searchSystemUser_userType")) #Klik Selection Menu
        pilih.select_by_visible_text('Admin') #pilih role Admin
        browser.find_element(By.ID,"searchBtn").click() # klik button Search
        time.sleep(1)

        # validasi
        browser.find_element(By.ID,"search-results").is_displayed(); #Serch Result Ditampilkan
       

    def test_success_add_skils(self): 
        listskill = ["skill1", "skill2", "skill3", "skill4", "skill5", "skill6", "skill7", "skill8"]
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
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a/b").click() # klik menu admin
        time.sleep(1)
        browser.find_element(By.ID,"menu_admin_Qualifications").click() # klik menu Qualifications
        time.sleep(1)
        browser.find_element(By.ID,"menu_admin_viewSkills").click() # klik sub menu skilss
        time.sleep(1)

        # step create job title
        browser.find_element(By.ID,"btnAdd").click() # klik buttton add
        time.sleep(1)
        browser.find_element(By.ID,"skill_name").send_keys(random.choice(listskill)) # isi skill title
        time.sleep(1)
        browser.find_element(By.ID,"skill_description").send_keys("ini tes") # isi skill description
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click() # klik button save
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.CLASS_NAME,"fadable").text
        self.assertEqual(response_message, 'Successfully Saved')

    def test_delete_skill(self): 
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
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a/b").click() # klik menu admin
        time.sleep(1)
        browser.find_element(By.ID,"menu_admin_Qualifications").click() # klik menu User Management
        time.sleep(1)
        browser.find_element(By.ID,"menu_admin_viewSkills").click() # klik Users
        time.sleep(1)

        # step create job title
        browser.find_element(By.XPATH,"//*[@id='recordsListTable']/tbody/tr[27]/td[1]/input").click() # klik Users
        time.sleep(1)
        browser.find_element(By.ID,"btnDel").click() # klik button save
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.CLASS_NAME,"fadable").text
        self.assertEqual(response_message, 'Successfully Deleted')
 

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()