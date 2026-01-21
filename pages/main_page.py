import allure
import time
from curl import Url
from locators.main_page_locators import MainPageLocators

from .base_page import BasePage


class MainPage(BasePage):
    @allure.step("Открыть главную страницу учебного тренажера Stellar Burgers")
    def open_main_page(self):
        self.open_page(Url.MAIN_PAGE_URL)

    @allure.step("Нажать на кнопку Личный кабинет")
    def click_on_account_button(self):
        self.wait_until_element_to_be_clickable(MainPageLocators.ACCOUNT_BUTTON)
        self.click_on_element(MainPageLocators.ACCOUNT_BUTTON)

    @allure.step("Нажать на кнопку Конструктор")
    def click_on_constructor_button(self):
        self.wait_until_element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Ожидание закрытия модального окна")
    def wait_modal_overlay_closed(self):
        self.wait_until_element_invisible(MainPageLocators.MODAL_OVERLAY)

    @allure.step("Нажать на кнопку Лента заказов")
    def click_on_order_lenta_button(self):
        self.wait_modal_overlay_closed()
        self.wait_until_element_to_be_clickable(MainPageLocators.ORDER_LENTA_BUTTON)
        self.click_on_element(MainPageLocators.ORDER_LENTA_BUTTON)

    @allure.step("Нажать на кнопку Оформить заказ")
    def click_on_do_order_button(self):
        self.wait_until_element_to_be_clickable(MainPageLocators.DO_ORDER_BUTTON)
        self.click_on_element(MainPageLocators.DO_ORDER_BUTTON)

    @allure.step("Нажать на ингредиент")
    def click_on_ingredient(self):
        self.wait_until_element_to_be_clickable(MainPageLocators.INGREDIENT_BUN_BUTTON)
        self.click_on_element(MainPageLocators.INGREDIENT_BUN_BUTTON)

    @allure.step("Получить текст окна")
    def window_text(self):
        return self.get_text(MainPageLocators.WINDOW_DETAILS_INGREDIENT)

    # Закрыть окно кликнув на крестик
    @allure.step("Закрыть окно Ингредиента нажав на крестик")
    def click_Window_closed_cross_button(self):
        self.wait_element(MainPageLocators.CLOSE_CARD_BUTTUN)
        self.click_on_element(MainPageLocators.CLOSE_CARD_BUTTUN)

    @allure.step("Страница отображает надпись Соберите бургер")
    def wait_visibility_text_constructor_burger(self):
        self.wait_element(MainPageLocators.TEXT_CONCTUCTOR_BURGER)
        return self.get_text(MainPageLocators.TEXT_CONCTUCTOR_BURGER)

    @allure.step("Поместить ингредиент в корзину")
    def add_ingredient_to_the_basket(self):
        self.wait_element(MainPageLocators.INGREDIENT_BUN_BUTTON)
        self.add_to_the_basket(
            MainPageLocators.INGREDIENT_BUN_BUTTON, MainPageLocators.BASKET
        )

    @allure.step("Получить количество ингредиента")
    def get_count_ingredient(self):
        return self.get_text(MainPageLocators.INGREDIENT_COUNT)

    @allure.step("Отображение окна с номером заказа")
    def id_window_is_displayed(self):
        self.wait_element(MainPageLocators.CLOSE_ORDER_NUMBER_BUTTUN)
        self.wait_until_element_to_be_clickable(
            MainPageLocators.CLOSE_ORDER_NUMBER_BUTTUN
        )
        time.sleep(5)
        self.wait_element(MainPageLocators.ORDER_NUMBER) # ORDER_ID
        return self.element_is_displayed(MainPageLocators.ORDER_NUMBER) # ORDER_ID

    # Закрыть окно кликнув на крестик
    @allure.step("Закрыть окно Номер заказа нажав на крестик")
    def сlick_closed_cross_button_Window_number_order(self):
        self.wait_element(MainPageLocators.CLOSE_ORDER_NUMBER_BUTTUN)
        self.click_via_js(MainPageLocators.CLOSE_ORDER_NUMBER_BUTTUN)
   
    # Получить номер заказа
    @allure.step("Получить номер заказа")
    def get_order_number(self):
        self.wait_until_element_invisible(MainPageLocators.MODAL_OVERLAY)
        self.find_element_with_wait(MainPageLocators.ORDER_NUMBER)
        return self.get_text(MainPageLocators.ORDER_NUMBER)
