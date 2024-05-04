from selene import browser, have
from allure import step


class CartPage:
    @staticmethod
    def should_have_item_added(item_label):
        with step(f"Checking item quantity and {item_label} label in cart"):
            browser.element(".qty-input").should(have.value("1"))
            browser.element(".product-name").should(have.text(item_label))

    @staticmethod
    def clear_cart():
        with step("Removing item from cart"):
            for element in browser.all(".qty-input"):
                element.clear()
                element.type("0").press_enter()


cart_page = CartPage()
