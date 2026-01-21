import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_page import OrderPage
from curl import Url
from data import Data


class TestOrderList:



    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_orde_in_work(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_on_account_button()
        login_page = LoginPage(driver)
        login_page.login_account(Data.data)
        main_page.add_ingredient_to_the_basket()
        main_page.click_on_do_order_button()
        main_page.id_window_is_displayed()
        main_page.сlick_closed_cross_button_Window_number_order()
        #         order_number = main_page.get_order_number() # нужно дописать ---






