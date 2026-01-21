import allure
from pages.main_page import MainPage
from curl import Url



class TestDoOrder:
    @allure.step("При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается")
    def test_add_ingredient_to_order_counter_for_that_ingredient_increases(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.add_ingredient_to_the_basket()
        assert main_page.get_count_ingredient() == '2'
    
    @allure.step('Проверка перехода по клику на «Конструктор»')
    def test_click_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_on_account_button()
        main_page.click_on_constructor_button()
        assert main_page.get_current_url() == Url.MAIN_PAGE_URL
        
    @allure.step("Переход по клику на раздел «Лента заказов»")
    def test_click_on_order_lenta(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_on_order_lenta_button()
        assert main_page.get_current_url() == Url.order_lenta_page

    @allure.step("Еcли кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_click_on_ingredient_popup_window_appear_with_details(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_on_ingredient()
        assert main_page.window_text() == 'Детали ингредиента'

    @allure.step("Всплывающее окно закрывается кликом по крестику")
    def test_popup_window_closed_by_clicking_on_the_cross_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_on_ingredient()
        main_page.click_Window_closed_cross_button()
        assert main_page.wait_visibility_text_constructor_burger() == 'Соберите бургер'




        
        

       


