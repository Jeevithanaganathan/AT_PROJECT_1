from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class OrangeHRM_delete():

    def test(self):
        driver = webdriver.Chrome()

        baseurl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

        # Open_the_website:
        driver.get(baseurl)

        # maximize the window
        driver.maximize_window()
        time.sleep(4)

        driver.implicitly_wait(5)

        # TC_login_01 A) Successful_Employee_login:

        """

        1.login panel, enter the username (Test Data: " Admin")
        2.Enter the password for the ESS-User account in the password field (Test data: "admin123")
        3.Click "login" button

                """

        xpath_of_username = "//input[@name='username']"

        xpath_of_password = "//input[@name='password']"

        xpath_of_login = "//button[@type='submit']"

        driver.find_element(By.XPATH, xpath_of_username).send_keys("Admin")

        driver.find_element(By.XPATH, xpath_of_password).send_keys("admin123")

        driver.find_element(By.XPATH, xpath_of_login).click()

        time.sleep(5)

        # TC_PIM_02 : Delete an existing_employee:

        """
        1.Go to PIM module from the left pane in the web page.
        2.From the existing list of employees in PIM module, delete an existing employee 
        """

        Xpath_of_PIM = "//a[contains(@href,'viewPimModule')]"
        PIM = driver.find_element(By.XPATH, Xpath_of_PIM)
        PIM.click()
        time.sleep(3)

        Xpath_of_Employee_list = "//a[text()='Employee List']"
        Employee_list = driver.find_element(By.XPATH, Xpath_of_Employee_list)
        Employee_list.click()
        time.sleep(3)

        Xpath_of_delete = "//button[@type='button']//following::button[13]"
        delete = driver.find_element(By.XPATH, Xpath_of_delete)
        delete.click()
        time.sleep(3)

        Xpath_of_delete_1 = "//button[@class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']"
        delete_1 = driver.find_element(By.XPATH, Xpath_of_delete_1)
        delete_1.click()
        time.sleep(3)

ab = OrangeHRM_delete()
ab.test()