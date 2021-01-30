from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "Basket empty message is not presented!"
    
    def should_be_empty(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty!"
        
    def should_not_be_empty(self):
        assert not self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is empty!"
