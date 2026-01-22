from selenium.webdriver.common.by import By


class LoginPageLocators:
    INPUT_IMAIL = (By.XPATH, "//input[contains(@class, 'input__textfield') and contains(@class, 'text_type_main-default') and @name='name']")  # На  https://stellarburgers.education-services.ru/login поле ввода почты
    INPUT_PASSWORD = By.XPATH, "//label[text()='Пароль']/following-sibling::input" # На  https://stellarburgers.education-services.ru/login поле ввода пароля
    LOGIN_BUTTON = By.XPATH, "//button[text()='Войти']" # На  https://stellarburgers.education-services.ru/login кнопка Войти
    