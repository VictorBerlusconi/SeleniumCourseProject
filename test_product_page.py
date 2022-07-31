from .pages.product_page import ProductPage
from selenium.webdriver.common.by import By
import sys
import pytest
import time

sys.path.insert(1, 'D:\\System\\Documents\\Python\\SeleniumCourseProject\\pages')
from .pages.locators import ProductPageLocators


# def test_add_to_cart_button_is_present(browser):
#    link = ProductPageLocators.PAGE_URL2
#    page = ProductPage(browser, link)
#    page.open()
#    page.is_element_present(By.CSS_SELECTOR, "[value='Добавить в корзину']")


# def test_add_to_cart(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#    page = ProductPage(browser, link)
#    page.open()
#    page.click_add_to_cart_button()
#    page.solve_quiz_and_get_code()
#    #time.sleep(100)

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    # link = ProductPageLocators.PAGE_URL2
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_cart_button()
    page.solve_quiz_and_get_code()
    page.is_item_added_to_cart()
    page.is_price_correct()
    # time.sleep(10)
