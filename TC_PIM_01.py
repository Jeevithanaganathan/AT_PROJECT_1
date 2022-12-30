from selenium import webdriver
from selenium.webdriver import ActionChains
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

        Xpath_of_Employee_id = '//label[text()="Employee Id"]//following::div[1]/input[1]'
        Employee_id = driver.find_element(By.XPATH, Xpath_of_Employee_id)
        Employee_id.click()
        time.sleep(3)

        Employee_id = driver.find_element(By.XPATH, Xpath_of_Employee_id)
        Employee_id.clear()
        time.sleep(3)

        Employee_id = driver.find_element(By.XPATH, Xpath_of_Employee_id)
        Employee_id.send_keys("5109")
        time.sleep(3)

        Xpath_of_save = "// button[@type='submit']"
        Save = driver.find_element(By.XPATH,Xpath_of_save)
        Save.click()
        time.sleep(2)

        Xpath_of_personal_details = "//a[@class='orangehrm-tabs-item --active']"
        personal_details = driver.find_element(By.XPATH,Xpath_of_personal_details)
        personal_details.click()
        time.sleep(2)

        Xpath_of_nickname = "//label[text()='Nickname']/following::div[1]/input"
        nickname = driver.find_element(By.XPATH,Xpath_of_nickname)
        nickname.clear()
        nickname.send_Keys("Prathi")
        time.sleep(3)

        Xpath_of_other_id = "//label[text()='Other Id']/following::div[1]/input"
        other_id = driver.find_element(By.XPATH,Xpath_of_other_id)
        other_id.send_keys("002")
        time.sleep(3)

        Xpath_of_lc_no = "//label[text()='Other Id']/following::input[2]"
        lc_no = driver.find_element(By.XPATH, Xpath_of_lc_no)
        lc_no.send_keys("LN1")
        time.sleep(3)

        Xpath_of_lc_Expiry_date = "//input[@placeholder='yyyy-mm-dd'][1]"
        lc_Expiry_date = driver.find_element(By.XPATH, Xpath_of_lc_Expiry_date)
        lc_Expiry_date.send_keys("2024-12-12")
        time.sleep(3)

        Xpath_of_SSN = "//input[@class='oxd-input oxd-input--active']/following::input[9]"
        SSN = driver.find_element(By.XPATH,Xpath_of_SSN)
        SSN.send_keys("12345")
        time.sleep(3)

        Xpath_of_SIN = "//input[@class='oxd-input oxd-input--active']/following::input[10]"
        SIN = driver.find_element(By.XPATH,Xpath_of_SIN)
        SIN.send_keys("678901")
        time.sleep(5)

        Xpath_of_nationality = "//*[text()='Nationality']/following::div[1]"
        nationality = driver.find_element(By.XPATH,Xpath_of_nationality)
        action = ActionChains(driver)
        action_1 = ActionChains(driver).move_to_element(nationality).click()
        action_1.perform()
        Xpath_of_select_role = "//div[@role='option']/span[text()='Indian']"
        select_role = driver.find_element(By.XPATH,Xpath_of_select_role)
        action_2 = ActionChains(driver).move_to_element(select_role).click()
        action_2.perform()
        time.sleep(3)

        Xpath_of_marital_status = "//label[text()='Marital Status']"
        marital_status = driver.find_element(By.XPATH, Xpath_of_marital_status)
        action_3 = ActionChains(driver)
        action_4 = ActionChains(driver).move_to_element(marital_status).click()
        action_3.perform()
        Xpath_of_selection_role_1 = "//label[text()='Marital Status']/following::div[1]"
        selection_role_1 = driver.find_element(By.XPATH,Xpath_of_selection_role_1)
        action_4 = ActionChains(driver).move_to_element(selection_role_1).click()
        action_4.perform()
        time.sleep(3)


        Xpath_of_save_1 = '//p[text()=" * Required"]/following::button[@type="submit"]'
        save_1 = driver.find_element(By.XPATH,Xpath_of_save_1)
        save_1.click()
        time.sleep(5)


ab = OrangeHRM_Add_employee()
ab.test()