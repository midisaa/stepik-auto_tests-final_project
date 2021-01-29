from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
#    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[class='col-sm-6 product_main'] h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "[class='col-sm-6 product_main'] .price_color")
    MESSAGE_PRODUCT_ADDED = (By.CSS_SELECTOR, "[class='alert alert-safe alert-noicon alert-success  fade in']:nth-child(1)")
    PRODUCT_NAME_ADDED = (By.CSS_SELECTOR, "[class='alert alert-safe alert-noicon alert-success  fade in']:nth-child(1) strong")
    MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, "[class='alert alert-safe alert-noicon alert-info  fade in']")
    BASKET_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "[class='alert alert-safe alert-noicon alert-info  fade in'] strong")
