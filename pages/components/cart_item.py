class CartItemComponent:
    def __init__(self, page):
        self.page = page
        self.cart_item = self.page.locator(".cart_item")
        self.cart_item_with_name = ".cart_item:has-text('{}')"
        self.cart_item_quantity = self.cart_item_with_name + " .summary_quantity"
        self.cart_item_price = self.cart_item_with_name + " .inventory_item_price"

    def get_cart_item_with_name(self, item_name):
        return self.page.locator(self.cart_item_with_name.format(item_name))

    def get_cart_item_price(self, item_name):
        return self.page.locator(self.cart_item_price.format(item_name))

    def get_cart_item_quantity(self, item_name):
        return self.page.locator(self.cart_item_quantity.format(item_name))

    def remove_item_with_name(self, item_name):
        self.get_cart_item_with_name(item_name).get_by_role('button', name='REMOVE').click()
