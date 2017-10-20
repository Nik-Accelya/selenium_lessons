from nose.tools import assert_equals
from selenium import webdriver
from framework.pages.loginPage import loginPage
from framework.pages.headerPage import headerPage


class testLogin():

    baseUrl = "http://twiindan.pythonanywhere.com/admin"

    @classmethod
    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.login_page = loginPage(self.driver)


    def setup(self):
        self.login_page.navigate()


    def test_incorrect_login(self):
        self.login_page.locate_elements()
        self.login_page.fillUsername('user2')
        self.login_page.fillPassword('fakepassword')
        self.login_page.submitClick()
        errorUrl = self.login_page.verifyURL()
        assert_equals('http://twiindan.pythonanywhere.com/admin/login/?next=/admin/', errorUrl)


    def test_correct_login(self):
        self.login_page.locate_elements()
        self.login_page.fillUsername('user1')
        self.login_page.fillPassword('selenium')
        self.login_page.submitClick()
        header_page = headerPage(self.driver)
        header_page.logout()


    @classmethod
    def teardown_class(self):
        self.driver.quit()


