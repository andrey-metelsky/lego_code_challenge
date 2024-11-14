
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.shopping_cart_btn = self.page.locator(".shopping_cart_container")

    @property
    def shopping_cart_counter(self):
        return self.page.locator(".fa-layers-counter")

    def open_shopping_cart(self):
        self.shopping_cart_btn.click()

    def get_locale(self) -> str:
        """Returns the current locale of the website."""
        return self.page.evaluate("navigator.language")
