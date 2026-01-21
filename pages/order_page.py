import allure
from .base_page import BasePage
from locators.order_list_page_locator import OrderListPageLocators

class OrderPage(BasePage):
    @allure.step('Количество заказов за все время')
    def get_all_orders_count(self):
        self.wait_element(OrderListPageLocators.ALL_ORDERS_COUNT)
        return self.get_text(OrderListPageLocators.ALL_ORDERS_COUNT)
    
    @allure.step('Количество заказов за сегодня')
    def get_today_orders_count(self):
        self.wait_element(OrderListPageLocators.TODAY_ORDERS_COUNT)
        return self.get_text(OrderListPageLocators.TODAY_ORDERS_COUNT)
    
    @allure.step('Получить номер заказа в работе')
    def get_order_in_work(self):
        self.wait_element(OrderListPageLocators.ORDER_IN_WORK)
        return self.get_text(OrderListPageLocators.ORDER_IN_WORK)
