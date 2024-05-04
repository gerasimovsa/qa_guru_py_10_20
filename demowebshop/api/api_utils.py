from utils.utils import post_demowebshop
from selene import browser
from allure import step


API_URL = "https://demowebshop.tricentis.com"
LOGIN_API = "/login"


class ApiUtils:
    @staticmethod
    def get_auth_cookie(login, password):
        with step(f"Getting auth cookie for Login: {login}, Password: {password}"):
            payload = {"Email": login, "Password": password}
            response = post_demowebshop(url=API_URL + LOGIN_API, data=payload, allow_redirects=False)
            return response.cookies.get("NOPCOMMERCE.AUTH")

    @staticmethod
    def authorize_user(auth_cookie):
        with step(f"Opening {API_URL} with {auth_cookie} auth cookie"):
            browser.open(API_URL)
            browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": auth_cookie})
            browser.open(API_URL)

    @staticmethod
    def add_item_to_cart(item_url):
        with step(f"Adding item with {item_url} url to cart"):
            auth_cookie = browser.driver.get_cookie("NOPCOMMERCE.AUTH")
            response = post_demowebshop(url=API_URL + item_url, cookies={auth_cookie["name"]: auth_cookie["value"]})
            return response


api_utils = ApiUtils()
