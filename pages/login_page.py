from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "You are not on login page!"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented!"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented!"

    def register_new_user(self, browser, email, password):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_EMAIL), "Email field on register form is not presented!"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_PASS), "Password field on register form is not presented!"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_PASS_CONFIRM), "Password confirm field on register form is not presented!"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Register button on register form is not presented!"
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        pass_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASS)
        pass_field_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASS_CONFIRM)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        email_field.send_keys(email)
        pass_field.send_keys(password)
        pass_field_confirm.send_keys(password)
        register_button.click()
        browser.implicitly_wait(10)
        assert self.is_element_present(*MainPageLocators.REGISTER_SUCCESS_MESSAGE), "Registration is not success!"
        browser.implicitly_wait(0)
        
