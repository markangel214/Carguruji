import time


class Add:

    def __init__(self, driver):
        self.driver = driver
        self.women = "Women"
        self.list_view = "//i[@class='icon-th-list']"
        self.item_blouse = "//a[@class='product-name'][contains(text(),'Blouse')]"
        self.add_to_cart = "//span[contains(text(),'Add to cart')]"
        self.close_view = "//span[@class='cross']"
        self.view_cart = "//b[contains(text(),'Cart')]"

    def women_category_click(self):
        time.sleep(2)
        self.driver.find_element_by_link_text(self.women).click()

    def list_view_click(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.list_view).click()

    def item_blouse_click(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.item_blouse).click()

    def add_to_cart_click(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.add_to_cart).click()

    def close_view_click(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.close_view).click()

    def view_cart_click(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.view_cart).click()
