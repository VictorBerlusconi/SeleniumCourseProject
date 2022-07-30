from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    PAGE_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/" #this link works for --language=ru
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    PAGE_URL = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    PAGE_URL2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[value='Добавить в корзину']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[class='col-sm-6 product_main'] h1")
    MESSAGE = (By.CSS_SELECTOR, "[class='alertinner ']") #selector is not unique, use find_elements
    PRICE = (By.CSS_SELECTOR, "[class='col-sm-6 product_main'] .price_color")
    PRICE_IN_CART = (By.CSS_SELECTOR, "[class = 'alert alert-safe alert-noicon alert-info  fade in'] strong")

