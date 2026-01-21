import allure
from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from curl import Url


class LoginPage(BasePage):
    @allure.step('Ввести почту')
    def input_email(self, email):
        self.send_keys(LoginPageLocators.INPUT_IMAIL, email)

    @allure.step('Ввести пароль')
    def input_password(self, password):
        self.send_keys(LoginPageLocators.INPUT_PASSWORD, password)

    @allure.step('Нажать на кнопку Войти')
    def click_login_button(self):
        self.wait_element(LoginPageLocators.LOGIN_BUTTON)
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON)

    #@allure.step("Ожидание успешного входа в аккаунт")
    #def wait_for_login_success(self):

        # Ждём появления элемента главной страницы (конструктора)
        #self.wait_element(MainPageLocators.TEXT_CONCTUCTOR_BURGER)
        # Ждём исчезновения модального окна, если оно есть
        #self.wait_until_element_invisible(MainPageLocators.MODAL_OVERLAY)

    #@allure.step("Вход в аккаунт")
    #def login_account(self, data):
        #self.input_email(data["email"])
        #self.input_password(data["password"])
        #self.click_login_button()
        #self.click_login_button()
        #self.wait_for_login_success()
    
    @allure.step("Вход в аккаунт")
    def login_account(self, data):
        self.input_email(data["email"])
        self.input_password(data["password"])
        self.click_login_button()