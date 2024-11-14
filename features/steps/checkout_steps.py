from behave import given, when, then
from playwright.sync_api import expect

from resources.test_data.user_info import UserInfo
from utilities.utils import Utils


@given('the user is on the Checkout Overview page')
def user_is_on_summary_page(context):
    context.execute_steps('''
            given the user has items in the cart
                | item_name           |
                | Sauce Labs Backpack |
            when the user proceeds to the Checkout Overview page
        ''')


@when('the user proceeds to the Checkout Overview page')
def proceed_to_checkout_overview(context):
    context.product_listing_page.open_shopping_cart()
    context.shopping_cart_page.proceed_to_checkout()
    user_data = UserInfo()
    context.checkout_page.enter_user_information(user_data)
    context.checkout_page.proceed_to_checkout_overview()


@then("the user should see each item with the correct name, price, and quantity")
def assert_checkout_overview_data(context):
    context.items_data = context.table
    for row in context.table:
        expect(context.checkout_page.cart_item_component.get_cart_item_with_name(row['item_name'])).to_be_visible()
        expect(context.checkout_page.cart_item_component.get_cart_item_price(row['item_name'])).to_have_text(
            f"${row['item_price']}")
        expect(context.checkout_page.cart_item_component.get_cart_item_quantity(row['item_name'])).to_have_text(
            row['item_qty'])


@when('the user submits order')
def click_finish(context):
    context.checkout_page.click_finish()


@then("the user should see an order confirmation message")
def assert_order_confirmed(context):
    confirmation_message = Utils.get_localized_text("order_confirmation_message")
    expect(context.page.get_by_text(confirmation_message)).to_be_visible()
    expect(context.checkout_page.pony_express_logo).to_be_visible()
    expect(context.product_listing_page.shopping_cart_counter).not_to_be_visible()


@then('the total items cost should be the sum of individual item prices')
def assert_items_total_cost(context):
    items_total = 0
    for data in context.items_data:
        items_total += float(data['item_price']) * float(data['item_qty'])
    context.items_total_cost = items_total
    expect(context.checkout_page.items_total).to_have_text(f"Item total: ${items_total}")


@then('the tax should be {percent}% of the total items cost')
def assert_tax_cost(context, percent: str):
    tax = round(context.items_total_cost * int(percent) / 100, 2)
    context.tax_cost = tax


@then('the billing cost should be the total items cost plus tax')
def assert_billing_total(context):
    billing_total = context.items_total_cost + context.tax_cost
    expect(context.checkout_page.total).to_have_text(f"Total: ${billing_total}")
