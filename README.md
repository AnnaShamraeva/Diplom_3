# Diplom_3
 Автотесты для UI веб-приложение Stellar Burgers
 

## <h>Project: Автотесты для UI веб-приложение Stellar Burgers</h>

> Проверка основной функциональности:
переход по клику на «Конструктор» - test_click_constructor_button;
переход по клику на раздел «Лента заказов» - test_click_on_order_lenta;
если кликнуть на ингредиент, появится всплывающее окно с деталями - test_click_on_ingredient_popup_window_appear_with_details;
всплывающее окно закрывается кликом по крестику - test_popup_window_closed_by_clicking_on_the_cross_button;
при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается - test_add_ingredient_to_order_counter_for_that_ingredient_increases.

Раздел «Лента заказов»:
при создании нового заказа счётчик «Выполнено за всё время» увеличивается;
при создании нового заказа счётчик «Выполнено за сегодня» увеличивается;
после оформления заказа его номер появляется в разделе «В работе»</h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты и записать отчет:</h>

> pytest tests --alluredir=allure_results</h>

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve ./allure-results</h>

