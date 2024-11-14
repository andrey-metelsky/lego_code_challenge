from behave import given
from dotenv import load_dotenv
import os

load_dotenv()


@given('"{user_role}" is on the Product Listing page')
def user_is_on_the_product_listing(context, user_role: str):
    context.login_page.log_in(os.getenv(user_role), os.getenv('PASSWORD'))
