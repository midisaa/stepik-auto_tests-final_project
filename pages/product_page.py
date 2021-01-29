from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def click_add_basket_button(self):
        add_basket_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        add_basket_button.click()
        
    def should_be_message_product_added(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_ADDED), "Product added message is not presented!"
    
    def should_be_message_basket_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_PRICE), "Basket price message is not presented!"

    def return_product_names(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented!"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_ADDED), "Product name in product added message is not presented!"
        product_name_added = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADDED).text
        return product_name, product_name_added

    def return_product_prices(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented!"
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE_IN_MESSAGE), "Basket price in basket price message is not presented!"
        basket_price_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price, basket_price_in_message
    
    def should_message_match_product_name(self, product_name, product_name_added):
        assert product_name == product_name_added, "Product name in product added message doesn't match!"
    
    def should_message_match_product_price(self, product_price, basket_price_in_message):
        assert product_price ==  basket_price_in_message, "Product price in basket price message doesn't match!"
