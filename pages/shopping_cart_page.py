from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.components.cart_item import CartItemComponent


class ShoppingCartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.cart_item_component = CartItemComponent(page)
        self.checkout_button = self.page.locator('.checkout_button')

    def proceed_to_checkout(self):
        self.checkout_button.click()
