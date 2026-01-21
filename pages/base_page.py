#from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    StaleElementReferenceException,
    ElementClickInterceptedException,
)

from selenium.webdriver.common.by import By


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


    # Подождать когда элемент станет кликабелен +
    def wait_until_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 45).until(EC.element_to_be_clickable(locator))

    # Получить текст +
    def get_text(self, locator):
        return self.driver.find_element(*locator).text

   

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

    # Ожидание исчезновения элемента
    def wait_until_element_invisible(self, locator):
        WebDriverWait(self.driver, 25).until(
            EC.invisibility_of_element_located(locator)
        )



    def click_on_element(self, locator: tuple, timeout: int = 12) -> None:
        """Оптимизированный метод клика с обработкой перекрытий и устаревших элементов."""
        wait = WebDriverWait(self.driver, timeout)
    
        try:
            elem = wait.until(EC.element_to_be_clickable(locator))
            elem.click()
            return

        except StaleElementReferenceException:
        # Элемент устарел — пробуем найти заново
            elem = wait.until(EC.element_to_be_clickable(locator))
            elem.click()
            return

        except ElementClickInterceptedException:
        # Если элемент перекрыт (Overlay)
            overlay_locators = [
                (By.CSS_SELECTOR, "div.Modal_modal__contentBox__sCy8X"),
                (By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr"),
            ]
        
            for o in overlay_locators:
                try:
                # Ожидаем исчезновения оверлея
                    WebDriverWait(self.driver, 3).until(EC.invisibility_of_element_located(o))
                    elem = wait.until(EC.element_to_be_clickable(locator))
                    elem.click()
                    return
                except Exception:
                    continue

        # Крайняя мера: клик через JavaScript, если обычный клик заблокирован
            elem = wait.until(EC.presence_of_element_located(locator))
            self.driver.execute_script(
                "arguments[0].scrollIntoView(true); arguments[0].click();", 
                elem
            )