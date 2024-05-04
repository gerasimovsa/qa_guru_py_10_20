import os

from data.items import *
from demowebshop.api.api_utils import api_utils
from demowebshop.pages.cart_page import cart_page
from demowebshop.pages.main_page import main_page


def test_add_book_to_cart():
    main_page.should_have_user_logged_in(os.getenv("LOGIN"))
    api_utils.add_item_to_cart(BOOK_ITEM["api"])
    main_page.should_have_item_added_to_cart()
    main_page.go_to_cart()

    cart_page.should_have_item_added(BOOK_ITEM["label"])

    cart_page.clear_cart()


def test_add_belt_to_cart():
    main_page.should_have_user_logged_in(os.getenv("LOGIN"))
    api_utils.add_item_to_cart(BELT_ITEM["api"])
    main_page.should_have_item_added_to_cart()
    main_page.go_to_cart()

    cart_page.should_have_item_added(BELT_ITEM["label"])

    cart_page.clear_cart()


def test_add_album_to_cart():
    main_page.should_have_user_logged_in(os.getenv("LOGIN"))
    api_utils.add_item_to_cart(ALBUM_ITEM["api"])
    main_page.should_have_item_added_to_cart()
    main_page.go_to_cart()

    cart_page.should_have_item_added(ALBUM_ITEM["label"])

    cart_page.clear_cart()


def test_add_jewelry_to_cart():
    main_page.should_have_user_logged_in(os.getenv("LOGIN"))
    api_utils.add_item_to_cart(JEWELRY_ITEM["api"])
    main_page.should_have_item_added_to_cart()
    main_page.go_to_cart()

    cart_page.should_have_item_added(JEWELRY_ITEM["label"])

    cart_page.clear_cart()
