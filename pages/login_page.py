from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.username_input = self.page.locator("#user-name")
        self.password_input = self.page.locator("#password")
        self.login_button = self.page.locator("#login-button")
        self.error_message = self.page.get_by_test_id("error")

    def fill_in_username(self, username):
        self.username_input.fill(username)

    def fill_in_password(self, password):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()

    def log_in(self, username, password):
        self.fill_in_username(username)
        self.fill_in_password(password)
        self.click_login()

