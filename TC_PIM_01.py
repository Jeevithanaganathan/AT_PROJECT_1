from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class OrangeHRM_Add_employee():

    def test(self):
        driver = webdriver.Chrome()

        baseurl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

        # Open_the_website:
        driver.get(baseurl)

        # maximize the window
        driver.maximize_window()
        time.sleep(4)

        driver.implicitly_wait(10)

        # TC_login_01 A) Successful_Employee_login:

        """
        Steps:
        1.login panel, enter the username (Test Data: " Admin")
        2.Enter the password for the ESS-User account in the password field (Test data: "admin123")
        3.Click "login" button

                """

        xpath_of_username = "//input[@name='username']"

        xpath_of_password = "//input[@name='password']"

        xpath_of_login = "//button[@type='submit']"
        # username:
        username = driver.find_element(By.XPATH, xpath_of_username)
        username.send_keys("Admin")
        # password:
        password = driver.find_element(By.XPATH, xpath_of_password)
        password.send_keys("admin123")
        # login:
        login = driver.find_element(By.XPATH, xpath_of_login)
        login.click()

        time.sleep(3)

        # TC_PIM_01 A) Add_new_employee:
        """
        1. Go to PIM Module from left panel in the web page
        2. Click on Add and and new employee details in the page
        3. Fill in all personal details of the employee and click save
        """

        xpath_of_PIM = "//a[contains(@href,'viewPimModule')]"
        xpath_of_add_button = "//button[@type='button']/following::button[4]"
        xpath_of_firstName = "//input[@name='firstName']"
        xpath_of_middleName = "//input[@name='middleName']"
        xpath_of_lastName = "//input[@name='lastName']"

        PIM = driver.find_element(By.XPATH, xpath_of_PIM)
        PIM.click()
        time.sleep(3)

        Add = driver.find_element(By.XPATH, xpath_of_add_button)
        Add.click()
        time.sleep(3)

        firstName = driver.find_element(By.XPATH, xpath_of_firstName)
        firstName.send_keys("Pradeepa")
        time.sleep(3)

        middleName = driver.find_element(By.XPATH, xpath_of_middleName)
        middleName.send_keys("Naganathan")
        time.sleep(3)

        lastName = driver.find_element(By.XPATH, xpath_of_lastName)
        lastName.send_keys("P")
        time.sleep(3)

        Employee_id = driver.find_element(By.XPATH, '//*[text()="Employee Id"]/following::input[1]')
        Employee_id.click()
        time.sleep(3)

        Employee_id = driver.find_element(By.XPATH, '//*[text()="Employee Id"]/following::input[1]')
        Employee_id.clear()
        time.sleep(3)

        Employee_id = driver.find_element(By.XPATH, '//*[text()="Employee Id"]/following::input[1]')
        Employee_id.send_keys("5109")
        time.sleep(3)

        Save = driver.find_element(By.XPATH, "// button[@type='submit']")
        Save.click()
        time.sleep(3)


ab = OrangeHRM_Add_employee()
ab.test()