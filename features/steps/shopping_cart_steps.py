from behave import given, when, then
from playwright.sync_api import expect


@given("the user has items in the cart")
@when('the user adds items to cart')
def add_items_to_cart(context):
    context.cart_items = []
    for row in context.table:
        context.product_listing_page.add_item_to_cart(row['item_name'])
        context.cart_items.append(row['item_name'])


@when("the user removes several items")
def remove_items_from_cart(context):
    for row in context.table:
        context.product_listing_page.remove_item(row['item_name'])
        context.cart_items.remove(row['item_name'])


@then("the cart counter should display the expected number of items")
def assert_cart_counter(context):
    expect(context.product_listing_page.shopping_cart_counter).to_have_text(str(len(context.cart_items)))


@then("the items should appear in the cart")
@then("only not removed items should remain in the cart")
def assert_items_in_cart(context):
    context.product_listing_page.shopping_cart_btn.click()
    expect(context.shopping_cart_page.cart_item_component.cart_item).to_have_count(len(context.cart_items))
    for item in context.cart_items:
        expect(context.shopping_cart_page.cart_item_component.cart_item.filter(has_text=item)).to_have_count(1)


