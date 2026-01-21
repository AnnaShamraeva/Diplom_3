from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Открыть страницу +
    def open_page(self, url):
        self.driver.get(url)

    # Получить url текущей страницы +
    def get_current_url(self):
        return self.driver.current_url

    # Ссылка работает - осуществляется переход
    def cross_url(self, url):
        WebDriverWait(self.driver, 15).until(EC.url_to_be(url))

    # Найти элемент +
    def find_element(self, locator):
        self.driver.find_element(*locator)

    # Подождать элемент +
    def wait_element(self, locator):
        WebDriverWait(self.driver, 45).until(EC.visibility_of_element_located(locator))

    # Нажать на элемент +
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    # Подождать когда элемент станет кликабелен +
    def wait_until_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 45).until(EC.element_to_be_clickable(locator))

    # Получить текст +
    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    # Добавить в корзину
    # def add_to_the_basket(self, element, endpoint):
    # element = self.driver.find_element(*element) # находит элемент, который нужно перетащить
    # endpoint = self.driver.find_element(*endpoint) # находит элемент-приёмник (корзину)
    # ActionChains(self.driver).drag_and_drop(element, endpoint).perform() # взятие элемента и перенос его в место назначения

    # Поиск элемента с ожиданием
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    # Добавить в корзину
    def add_to_the_basket(self, locator_sourse, locator_target):
        element = self.find_element_with_wait(
            locator_sourse
        )  # находит элемент, который нужно перетащить
        target = self.find_element_with_wait(
            locator_target
        )  # находит элемент-приёмник (корзину)
        drag_and_drop(
            self.driver, element, target
        )  # взятие элемента и перенос его в место назначения

    # Передать значения
    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    # Отображение элемента
    def element_is_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    # Клик через JavaScript (для обхода проблем с перекрытием элементов)
    def click_via_js(self, locator):
        element = WebDriverWait(self.driver, 45).until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].click();", element)
