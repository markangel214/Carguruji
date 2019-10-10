import time

class Login:

    def __init__(self, driver):
        self.driver = driver
        self.email = "//input[@id='email']"
        self.password = "//input[@id='passwd']"
        self.login_button = "//form[@id='login_form']//span[1]"
        self.logout_button = "//a[@class='logout']"

    def enter_email(self, email):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.email).send_keys(email)

    def enter_password(self, password):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.password).send_keys(password)

    def login_button_click(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.login_button).click()

    def logout_button_click(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.logout_button).click()

    def screen_shot_of_login(self):
        self.driver.execute_script("window.scrollBy(0,400)", "")
        self.driver.save_screenshot("/Users/admin3/Documents/notes/CarGuruji/ScreenShot/ScreenshotOfLogin.jpg")
        self.driver.get_screenshot_as_file("/Users/admin3/Documents/notes/CarGuruji/ScreenShot/ScreenshotOfLogin.jpg")

    def screen_shot_of_logout(self):
        self.driver.execute_script("window.scrollBy(0,400)", "")
        self.driver.save_screenshot("/Users/admin3/Documents/notes/CarGuruji/ScreenShot/ScreenshotOfLogout.jpg")
        self.driver.get_screenshot_as_file("/Users/admin3/Documents/notes/CarGuruji/ScreenShot/ScreenshotOfLogout.jpg")
