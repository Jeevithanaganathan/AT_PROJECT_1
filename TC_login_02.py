from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class OrangeHRM_invalid_login():

    def test(self):
        driver = webdriver.Chrome()

        baseurl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

        # Open_the_website:
        driver.get(baseurl)

        # maximize the window
        driver.maximize_window()
        time.sleep(4)

        driver.implicitly_wait(5)

        # TC_login_02 :invalid_Employee_login:
        """
         steps:
         
         1.login panel, enter the username (Test Data: " Admin")
         2.Enter the password for the ESS-User account in the password field (Test data: "Invalid password")
         3.Click "login" button
    
        """
        xpath_of_username = "//input[@name='username']"

        xpath_of_password = "//input[@name='password']"

        xpath_of_login = "//button[@type='submit']"
        #username:
        username = driver.find_element(By.XPATH, xpath_of_username)
        username.send_keys("Admin")

        #password:
        password = driver.find_element(By.XPATH, xpath_of_password)
        password.send_keys("invalid password")

        #login:
        login = driver.find_element(By.XPATH, xpath_of_login)
        login.click()

        time.sleep(5)

ab = OrangeHRM_invalid_login()
ab.test()
