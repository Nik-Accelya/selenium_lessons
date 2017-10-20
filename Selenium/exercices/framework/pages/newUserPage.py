from exercices.framework.core.base import BasePage
from exercices.framework.pages.userListPage import userListPage
from selenium.webdriver.support.ui import Select



class newUserPage(BasePage):
    url = "https://forum-testing.herokuapp.com/v1.0/users/new"

    _usernameTextBox = None
    _passwordTextBox = None
    _nameTextBox = None
    _emailTextBox = None
    _roleSelect = None


    def locate_elements(self):
        self._emailTextBox = self.driver.find_element_by_id('email')
        self._nameTextBox = self.driver.find_element_by_id('name')
        self._usernameTextBox = self.driver.find_element_by_id('username')
        self._passwordTextBox = self.driver.find_element_by_id('password')
        self._roleSelect = self.driver.find_element_by_id('role')
        self._saveButton = self.driver.find_element_by_id('save')

    def fill_name(self, name):
        self._nameTextBox.send_keys(name)

    def fill_username(self, username):
        self._usernameTextBox.send_keys(username)

    def fill_role(self, role):
        Select(self._roleSelect).select_by_visible_text(role)

    def fill_password(self, password):
        self._passwordTextBox.send_keys(password)

    def fill_email(self, email):
        self._emailTextBox.send_keys(email)

    def click_button(self):
        self._saveButton.click()
        return userListPage(self.driver)

    def fill_all_form(self, username, password, role, email, name):

        self.fill_username(username)
        self.fill_name(name)
        self.fill_password(password)
        self.fill_role(role)
        self.fill_email(email)
        self.click_button()
        return userListPage(self.driver)
