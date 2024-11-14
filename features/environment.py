from from_root import from_root
from playwright.sync_api import sync_playwright
from behave import fixture, use_fixture
from dotenv import load_dotenv
import os

from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.product_listing_page import ProductListingPage
from pages.shopping_cart_page import ShoppingCartPage

load_dotenv()
BASE_URL = os.getenv("BASE_URL")
LOGIN_PAGE_URL = f'{BASE_URL}/index.html'


@fixture
def page(context):
    with sync_playwright() as p:
        p.selectors.set_test_id_attribute('data-test')
        context.browser = p.chromium.launch(headless=True, args=["--start-maximized"])
        context.browser = context.browser.new_context(no_viewport=True, locale=os.getenv('LOCALE'))
        context.page = context.browser.new_page()
        context.page.goto(LOGIN_PAGE_URL)
        yield
        context.page.close()
        context.browser.close()


def before_scenario(context, scenario):
    use_fixture(page, context)
    context.login_page = LoginPage(context.page)
    context.product_listing_page = ProductListingPage(context.page)
    context.shopping_cart_page = ShoppingCartPage(context.page)
    context.checkout_page = CheckoutPage(context.page)

