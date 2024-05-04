import os

from allure import step
import pytest
from dotenv import load_dotenv
from selene import browser

from demowebshop.api.api_utils import api_utils


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="session", autouse=True)
def setup_browser():
    with step("Getting login and password from .env.example"):
        login = os.getenv("LOGIN")
        password = os.getenv("PASSWORD")
    with step("Setting up timeout for browser"):
        browser.config.timeout = 10.0
    with step("Setting up browser window size"):
        browser.config.window_width = 1920
        browser.config.window_height = 1200
    with step("Getting authorization cookie and authorizing user"):
        cookie = api_utils.get_auth_cookie(login, password)
        api_utils.authorize_user(cookie)

    yield

    with step("Quitting driver"):
        browser.quit()
