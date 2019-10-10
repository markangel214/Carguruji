import time
from selenium.webdriver.support.ui import Select

class New:

    def __init__(self, driver):
        self.driver = driver
        self.email = "//input[@id='email_create']"
        self.create_button = "//form[@id='create-account_form']//span[1]"
        self.first_name = "//input[@id='customer_firstname']"
        self.last_name = "//input[@id='customer_lastname']"
        self.password = "//input[@id='passwd']"
        self.birth_day = "//select[@id='days']"
        self.birth_month = "//select[@id='months']"
        self.birth_year = "//select[@id='years']"
        self.register_button = "//span[contains(text(),'Register')]"

    def enter_email(self, email):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.email).send_keys(email)

    def create_button_click(self):
        self.driver.find_element_by_xpath(self.create_button).click()

    def enter_full_name(self, first, last):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.first_name).send_keys(first)
        self.driver.find_element_by_xpath(self.last_name).send_keys(last)

    def enter_password(self, password):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.password).send_keys(password)

    def enter_birth_day(self, day):
        time.sleep(5)
        element = self.driver.find_element_by_xpath(self.birth_day)
        drop1 = Select(element)
        drop1.select_by_index(day)

    def enter_birth_month(self, month):
        time.sleep(5)
        element = self.driver.find_element_by_xpath(self.birth_month)
        drop1 = Select(element)
        drop1.select_by_index(month)

    def enter_birth_year(self, year):
        time.sleep(5)
        element = self.driver.find_element_by_xpath(self.birth_year)
        drop1 = Select(element)
        drop1.select_by_index(year)

    def register_click(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.register_button).click()

    def screen_shot_of_New_account(self):
        self.driver.save_screenshot("/Users/admin3/Documents/notes/CarGuruji/ScreenShot/ScreenshotOfRegister.jpg")
        self.driver.get_screenshot_as_file("/Users/admin3/Documents/notes/CarGuruji/ScreenShot/ScreenshotOfRegister.jpg")