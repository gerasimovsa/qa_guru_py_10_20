from selene import browser, have
from allure import step


class MainPage:
    @staticmethod
    def go_to_cart():
        with step("Opening cart"):
            browser.element("li#topcartlink").click()

    @staticmethod
    def should_have_user_logged_in(login):
        with step("Checking that user is authorized"):
            browser.element(".account").should(have.text(login))

    @staticmethod
    def should_have_item_added_to_cart():
        with step("Checking that cart label is updated after adding an item"):
            browser.driver.refresh()
            browser.element("span.cart-qty").should(have.no.text("(0)"))


main_page = MainPage()
