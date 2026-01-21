from selenium.webdriver.common.by import By


class MainPageLocators:
    MODAL_OVERLAY = (
        By.CSS_SELECTOR, 
        "div.Modal_modal__overlay, div.Modal_modal__loading__3534A, div[data-test='modal-overlay']"
        ) # Модальное окно (overlay) 
    
    ACCOUNT_BUTTON = (
        By.XPATH,
        "//p[@class='AppHeader_header__linkText__3q_va ml-2' and normalize-space(.)='Личный Кабинет']",
    )  # Кнопка "Личный кабинет" в хедере
    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//p[@class='AppHeader_header__linkText__3q_va ml-2' and normalize-space(.)='Конструктор']",
    )  # Кнопка "Конструктор"
    ORDER_LENTA_BUTTON = (
        By.XPATH,
        "//p[@class='AppHeader_header__linkText__3q_va ml-2' and normalize-space(.)='Лента Заказов']",
    )  # Кнопка "Лента заказов"
    INGREDIENT_BUN_BUTTON = (
        By.XPATH,
        "//img[@alt='Флюоресцентная булка R2-D3']",
    )  # Ингредиент булочка флюоресцентная
    WINDOW_DETAILS_INGREDIENT = (
        By.XPATH,
        "//h2[text()='Детали ингредиента']",
    )  # Окно детали ингредиента
    CLOSE_CARD_BUTTUN = (
        By.XPATH,
        "//button[contains(@class, 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK')]",
    )  # Кнопка закрытия карточки ингредиента
    TEXT_CONCTUCTOR_BURGER = (
        By.XPATH,
        "//*[local-name()='h1' and normalize-space(.)='Соберите бургер']",
    )
    BASKET = (
        By.XPATH,
        "//li[contains(@class,'BurgerConstructor_basket__listItem')]//div[contains(@class,'constructor-element')]",
    )  # Корзина
    INGREDIENT_COUNT = (
        By.XPATH,
        "//div[contains(@class,'counter_counter__ZNLkj') and contains(@class,'counter_default__28sqi')]//p[contains(@class,'counter_counter__num')]",
    )  # Счетчик ингредиента
    DO_ORDER_BUTTON = (
        By.XPATH,
        "//button[normalize-space(.)='Оформить заказ']",
    )  # Кнопка оформить заказ
    ORDER_ID = (
        By.XPATH,
        "//div[contains(@class,'Modal')]//p[normalize-space(.)='идентификатор заказа']",
    )  # Окно с идентификатором заказа

    # Кнопка закрыть карточку с номером заказа (уникальный локатор с контекстом модального окна заказа)
    CLOSE_ORDER_NUMBER_BUTTUN = (
        By.XPATH,
        "//div[contains(@class,'Modal') and .//p[contains(text(),'идентификатор заказа')]]//button[contains(@class,'Modal_modal__close')]",
    )  # Кнопка закрытия карточки с номером заказа
    ORDER_NUMBER = (
        By.XPATH,
        "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']" 
        
    )  # Номер заказа
