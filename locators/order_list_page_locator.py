from selenium.webdriver.common.by import By

class OrderListPageLocators:
   
   LAST_ORDER = By.XPATH, '//li[1]//p[(@class="text text_type_digits-default")]' # Последний заказ
   
   ORDER_IN_WORK =  By.XPATH, '//*[contains(@class, "orderListReady")]' # Заказ в работе
   ALL_ORDERS_COUNT = (
      By.XPATH, 
      "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class,'digits-large')]"
   ) # Выполнено за все время

   TODAY_ORDERS_COUNT =(
      By.XPATH, 
      "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class,'digits-large')]"
   )   # "Выполнено за сегодня:"