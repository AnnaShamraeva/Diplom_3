import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_page import OrderPage
from curl import Url
from data import Data


class TestOrderList:
    @allure.title('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_ordes_count_all_time_increase(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_on_account_button()
        login_page = LoginPage(driver)
        login_page.login_account(Data.data)
        main_page.click_on_order_lenta_button()
        order_page = OrderPage(driver)
        all_orders = order_page.get_all_orders_count()
        main_page.click_on_constructor_button()
        main_page.add_ingredient_to_the_basket()
        main_page.click_on_do_order_button()
        main_page.id_window_is_displayed() 
        main_page.сlick_closed_cross_button_Window_number_order()
        main_page.click_on_order_lenta_button()
        update_all_orders = order_page.get_all_orders_count()
        assert update_all_orders > all_orders
        

    @allure.title('при создании нового заказа счётчик Выполнено за сегодня')
    def test_ordes_count_today_increase(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_on_account_button()
        login_page = LoginPage(driver)
        login_page.login_account(Data.data)
        main_page.click_on_order_lenta_button()
        order_page = OrderPage(driver)
        today_orders = order_page.get_today_orders_count()
        main_page.click_on_constructor_button()
        main_page.add_ingredient_to_the_basket()
        main_page.click_on_do_order_button()
        main_page.id_window_is_displayed() 
        main_page.сlick_closed_cross_button_Window_number_order()
        main_page.click_on_order_lenta_button()
        update_today_orders = order_page.get_today_orders_count()
        assert update_today_orders > today_orders

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
        order_number = main_page.get_order_number()
        main_page.сlick_closed_cross_button_Window_number_order()
        main_page.click_on_order_lenta_button()
        order_page = OrderPage(driver)
        assert order_number in order_page.get_last_order_number()       







