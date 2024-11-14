from playwright.sync_api import Page

from pages.base_page import BasePage


class ProductListingPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.inventory_item = self.page.locator(".inventory_item")
        self.add_button = self.page.get_by_role('button', name="ADD TO CART")
        self.remove_button = self.page.get_by_role('button', name="REMOVE")

    def add_item_to_cart(self, item_name: str):
        self.inventory_item.filter(has_text=item_name).locator(self.add_button).click()

    def remove_item(self, item_name):
        self.inventory_item.filter(has_text=item_name).locator(self.remove_button).click()
