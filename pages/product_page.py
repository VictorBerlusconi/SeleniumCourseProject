from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
from selenium.common.exceptions import NoSuchElementException

class ProductPage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def click_add_to_cart_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def is_item_added_to_cart(self):
        messages = self.browser.find_elements(*ProductPageLocators.MESSAGE)
        message_item_added = messages[0]
        item_name = message_item_added.text
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name = product.text
        product_name_plus_message = product_name + " был добавлен в вашу корзину."
        assert item_name in product_name_plus_message, \
            f"Wrong product added to cart! Should be >{product_name_plus_message}< instead of >{item_name}<"

    def is_price_correct(self):
        price_in_cart_element = self.browser.find_element(*ProductPageLocators.PRICE_IN_CART)
        price_in_cart = price_in_cart_element.text
        price_element = self.browser.find_element(*ProductPageLocators.PRICE)
        price = price_element.text
        assert price in price_in_cart, \
            f"Wrong price is added to cart! Should be {price} instead of {price_in_cart}"
