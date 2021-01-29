from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest

@pytest.mark.skip
@pytest.mark.parametrize('promo', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='Bugged_link!')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_basket_button()
    page.solve_quiz_and_get_code()
    page.should_be_message_product_added()
    product_name, product_name_added = page.return_product_names()
    page.should_message_match_product_name(product_name, product_name_added)
    page.should_be_message_basket_price()
    product_price, basket_price_in_message = page.return_product_prices()
    page.should_message_match_product_price(product_price, basket_price_in_message)

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_basket_button()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail    
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_basket_button()
    page.should_success_message_dissapper()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.skip
#Тест для проверки, что локатор BASKET_ITEMS в BasketPageLocators актуален:
def test_guest_can_see_product_in_basket_after_adding_product(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_basket_button()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_empty()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty()
    basket_page.should_be_basket_empty_message()
