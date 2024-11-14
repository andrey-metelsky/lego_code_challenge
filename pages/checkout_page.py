from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.components.cart_item import CartItemComponent
from resources.test_data.user_info import UserInfo


class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        # User Information
        self.first_name_input = self.page.get_by_test_id('firstName')
        self.last_name_input = self.page.get_by_test_id('lastName')
        self.postal_code_input = self.page.get_by_test_id('postalCode')
        self.continue_button = self.page.get_by_role('button', name='CONTINUE')
        # Checkout Overview
        self.cart_item_component = CartItemComponent(page)
        self.items_total = self.page.locator('.summary_subtotal_label')
        self.tax = self.page.locator('.summary_tax_label')
        self.total = self.page.locator('.summary_total_label')
        self.finish_button = self.page.locator(".cart_button:has-text('FINISH')")
        # Finish
        self.pony_express_logo = self.page.locator('.pony_express')

    def enter_user_information(self, user_info: UserInfo):
        self.first_name_input.fill(user_info.first_name)
        self.last_name_input.fill(user_info.last_name)
        self.postal_code_input.fill(user_info.postal_code)

    def proceed_to_checkout_overview(self):
        self.continue_button.click()

    def click_finish(self):
        self.finish_button.click()

