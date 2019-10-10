from selenium.webdriver.support.ui import Select


class Checkout:

    def __init__(self, driver):
        self.driver = driver
        self.first_name = "//input[@id='firstname']"
        self.last_name = "//input[@id='lastname']"
        self.address = "//input[@id='address1']"
        self.city = "//input[@id='city']"
        self.state = "//select[@id='id_state']"
        self.zip_code = "//input[@id='postcode']"
        self.country = "//select[@id='id_country']"
        self.phone = "//input[@id='phone']"
        self.mobile = "//input[@id='phone_mobile']"
        self.address2 = "//input[@id='alias']"
        self.save = "//span[contains(text(),'Save')]"
        self.proceed11 = "Proceed to checkout"
        self.proceed22 = "//button[@name='processAddress']//span[contains(text(),'Proceed to checkout')]"
        self.proceed33 = "//button[@name='processCarrier']//span[contains(text(),'Proceed to checkout')]"
        self.bank = "//a[@class='bankwire']"
        self.confirm = "//span[contains(text(),'I confirm my order')]"

    def enter_full_name(self, first, last):
        self.driver.find_element_by_xpath(self.first_name).send_keys(first)
        self.driver.find_element_by_xpath(self.last_name).send_keys(last)
        self.driver.implicitly_wait(10)

    def enter_full_address(self, address, city, state, zip_code):
        self.driver.find_element_by_xpath(self.address).send_keys(address)
        self.driver.find_element_by_xpath(self.city).send_keys(city)
        state1 = Select(self.state)
        state1.select_by_visible_text(state)
        self.driver.find_element_by_xpath(self.zip_code).send_keys(zip_code)
        self.driver.implicitly_wait(10)

    def enter_phone_and_mobile(self, phone, mobile):
        self.driver.find_element_by_xpath(self.phone).send_keys(phone)
        self.driver.find_element_by_xpath(self.mobile).send_keys(mobile)
        self.driver.implicitly_wait(10)

    def enter_address2(self, address):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.address2).send_keys(address)

    def save_click(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.save).click()

    def proceed1(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text(self.proceed11).click()

    def proceed2(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.proceed22).click()

    def check(self):
        self.driver.find_element_by_xpath("//input[@id='cgv']").click()

    def proceed3(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.proceed33).click()

    def bank_click(self):
        self.driver.find_element_by_xpath(self.bank).click()

    def confirm_click(self):
        self.driver.find_element_by_xpath(self.confirm).click()

    def screen_shot_of_proceed(self):
        self.driver.save_screenshot("/Users/admin3/Documents/notes/CarGuruji/ScreenShot/ScreenshotOfProceed.jpg")
        self.driver.get_screenshot_as_file("/Users/admin3/Documents/notes/CarGuruji/ScreenShot/ScreenshotOfProceed.jpg")

    def screen_shot_of_cart(self):
        self.driver.save_screenshot("/Users/admin3/Documents/notes/CarGuruji/ScreenShot/ScreenshotOfCart.jpg")
        self.driver.get_screenshot_as_file("/Users/admin3/Documents/notes/CarGuruji/ScreenShot/ScreenshotOfCart.jpg")
