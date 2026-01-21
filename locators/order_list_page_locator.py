from selenium.webdriver.common.by import By

class OrderListPageLocators:
   ORDER = By.XPATH, '//li[contains(@class, "OrderHistory_listItem")]'
   LAST_ORDER = By.XPATH, '//li[1]//p[(@class="text text_type_digits-default")]'
   ORDER_WINDOW = By.XPATH, '//div[contains(@class, "Modal_orderBox")]'
   ORDER_IN_WORK =  By.XPATH, '//*[contains(@class, "orderListReady")]'
   ALL_ORDERS_COUNT =  By.XPATH, '//p[contains(@class, "text_type_main-medium") and normalize-space(.)="Выполнено за все время:"]'

   TODAY_ORDERS_COUNT = By.XPATH, '//p[contains(@class,"text_type_main-medium") and normalize-space(.)="Выполнено за сегодня:"]'