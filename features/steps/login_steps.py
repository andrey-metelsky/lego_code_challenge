from playwright.sync_api import expect
from behave import given, when, then

from pages.login_page import LoginPage
from dotenv import load_dotenv
import os

from utilities.utils import Utils

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
LOGIN_PAGE_URL = f'{BASE_URL}/index.html'
INVENTORY_PAGE_URL = f'{BASE_URL}/inventory.html'


@given("the user is on the login page")
def user_on_login_page(context):
    context.login_page = LoginPage(context.page)


@when('the user logs in as {username}')
def log_in(context, username: str):
    context.login_page.log_in(username=os.getenv(username), password=os.getenv('PASSWORD'))


@when("the user logs in with invalid: {invalid_field}")
def log_in_with_invalid_credentials(context, invalid_field: str):
    match invalid_field:
        case 'username':
            context.login_page.fill_in_username("invalid_username")
            context.login_page.fill_in_password(os.getenv('PASSWORD'))
        case 'password':
            context.login_page.fill_in_username(os.getenv("STANDARD_USER"))
            context.login_page.fill_in_password("invalid_password")
        case 'username and password':
            context.login_page.fill_in_username("invalid_username")
            context.login_page.fill_in_password("invalid_password")
        case _:
            raise ValueError(f"'{invalid_field}' is not expected field name")
    context.login_page.click_login()


@then("the user is successfully logged in")
def assert_successful_login(context):
    expect(context.page).to_have_url(INVENTORY_PAGE_URL)


@then("the user is not logged in")
def assert_unsuccessful_login(context):
    expect(context.page).to_have_url(os.getenv('LOGIN_PAGE_URL'))
    expect(context.login_page.username_input).to_be_visible()


@then("invalid credentials error message is displayed")
def assert_error_message(context):
    expected_error_text = Utils.get_localized_text("invalid_credentials_error")
    expect(context.login_page.error_message).to_have_text(expected_error_text)


@then("locked user error message is displayed")
def assert_error_message(context):
    expected_error_text = Utils.get_localized_text("locked_user_error")
    expect(context.login_page.error_message).to_have_text(expected_error_text)
