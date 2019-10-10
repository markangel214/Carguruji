import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from Page.Checkout import Checkout
from Page.NewAccount import New
from Page.Login import Login
from Page.Add import Add
import time


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/admin3/Documents/notes/chromedriver")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test1_new_account(self):
        self.driver.get("http://carguruji.com/shop/")
        self.driver.find_element_by_xpath("//a[@class='login']").click()
        self.driver.implicitly_wait(10)
        account = New(self.driver)
        account.enter_email("lasta@gmail.com")
        account.create_button_click()
        account.enter_full_name("Mark", "Ange")
        account.enter_password("123456")
        account.enter_birth_day(25)
        account.enter_birth_month(5)
        account.enter_birth_year(20)
        account.register_click()

    def test2_login_logout(self):
        self.driver.get("http://carguruji.com/shop/")
        self.driver.find_element_by_xpath("//a[@class='login']").click()
        self.driver.implicitly_wait(10)
        login = Login(self.driver)
        login.enter_email("lasta@gmail.com")
        login.enter_password("123456")
        login.login_button_click()
        title = self.driver.title
        self.assertEqual("My account - CarGuruji Shop", title, "You are Login")
        login.screen_shot_of_login()
        login.logout_button_click()
        title = self.driver.title
        self.assertEqual("Login - CarGuruji Shop", title, "You are now Log out")
        login.screen_shot_of_logout()

    def test3_add_and_proceed(self):
        self.driver.get("http://carguruji.com/shop/")
        self.driver.find_element_by_xpath("//a[@class='login']").click()
        self.driver.implicitly_wait(10)
        login = Login(self.driver)
        login.enter_email("bb@gmail.com")
        login.enter_password("mmmmmm")
        login.login_button_click()

        title = self.driver.title
        self.assertEqual("My account - CarGuruji Shop", title)

        add = Add(self.driver)
        add.women_category_click()
        add.list_view_click()
        add.item_blouse_click()
        add.add_to_cart_click()
        add.close_view_click()
        add.view_cart_click()

        title = self.driver.title
        self.assertEqual("Order - CarGuruji Shop", title)
        self.driver.implicitly_wait(10)

        checkout = Checkout(self.driver)
        self.driver.execute_script("window.scrollBy(0,400)", "")
        checkout.screen_shot_of_cart()
        checkout.proceed1()
        '''
        # Remove the comment mark of this if the user have no Shipment address
        checkout.enter_full_name("Mark", "Ange")
        checkout.enter_full_address("115", "Toronto", "Ohio", "22132")
        checkout.enter_phone_and_mobile("22222222222", "22222222222")
        checkout.enter_address2("My address")
        checkout.save_click()
        '''
        checkout.proceed2()
        checkout.check()
        checkout.proceed3()
        checkout.bank_click()
        checkout.confirm_click()
        self.driver.execute_script("window.scrollBy(0,400)", "")
        checkout.screen_shot_of_proceed()

    def tearDown(self):
        print("Test Complete!!!")
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
