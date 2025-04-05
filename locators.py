from selenium.webdriver.common.by import By


class LocatorsPwdPage:
    LK_BUTTON = [By.XPATH, '//a[@href="/account"]']
    RECOVERY_PASSWORD = [By.XPATH, '//a[text()="Восстановить пароль"]']
    MAIL_INPUT = [By.XPATH, '//label[text()="Email"]/following-sibling::input']
    RESTORE_BUTTON = [By.XPATH, '//button[text()="Восстановить"]']
    SAVE_PWD_BUTTON = [By.XPATH, '//button[text()="Сохранить"]']
    INPUT_NEW_PASSWORD = [By.XPATH, '//input[@name="Введите новый пароль"]']
    BUTTON_VISIBILITY_PASSWORD = [By.XPATH, ".//div[contains(@class, 'input__icon')]"]
    SEARCH_ELEMENT = [By.XPATH, ".//div[contains(@class, 'input_status_active')]"]

class LocatorsProfilePage:
    LK_BUTTON = [By.XPATH, '//a[@href="/account"]']
    PASSWORD_INPUT = [By.XPATH, "//*[text()='Пароль']/following-sibling::input"]
    MAIL_INPUT = [By.XPATH, "//*[text()='Email']/following-sibling::input"]
    BUTTON_ENTER = [By.XPATH, "//button[text()='Войти']"]
    BUTTON_PROFILE = [By.XPATH, "//a[text()='Профиль']"]
    ORDER_HISTORY = [By.XPATH, "//a[text()='История заказов']"]
    EXIT_BUTTON = [By.XPATH, '//button[text()="Выход"]']

class LocatorsConstructorPage:
    BUTTON_AUTH_ACCOUNT = [By.XPATH, "//button[contains(@class, 'button_button__33qZ0')]"]
    CONSTRUCTOR_BUTTON = [By.XPATH, '//a[@href="/"]']
    ORDER_FEED_BUTTON = [By.XPATH, '//a[@href="/feed"]']
    FLUORESCENT_BUN = [By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')]"]
    INGREDIENT_WINDOW = [By.XPATH, ".//h2[text()='Детали ингредиента']"]
    EXIT_INGREDIENT_WINDOW = [By.XPATH, ".//button[@type='button']"]
    INGREDIENT_COUNTER = [By.XPATH, '//p[@class="counter_counter__num__3nue1"]']
    INGREDIENT_BASKET = [By.XPATH, '//ul[@class="BurgerConstructor_basket__list__l9dp_"]/parent::section']
    PASSWORD_INPUT = [By.XPATH, "//*[text()='Пароль']/following-sibling::input"]
    MAIL_INPUT = [By.XPATH, "//*[text()='Email']/following-sibling::input"]
    BUTTON_ENTER = [By.XPATH, "//button[text()='Войти']"]
    SAUCE_SPACE_X = [By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa72"]']
    BEEF_METEORITE = [By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6f"]']
    CHECKOUT_BUTTON = [By.XPATH, '//button[text()="Оформить заказ"]']
    ORDER_PREPARED = [By.XPATH, '//p[text()="Ваш заказ начали готовить"]']

class LocatorsOrderPage:
    LAST_ORDER = (By.XPATH, ".//ul[@class='OrderFeed_list__OLh59']/li[1]")
    ORDER_FEED_BUTTON = [By.XPATH, '//a[@href="/feed"]']
    STRUCTURE = [By.XPATH, "//p[@class='text text_type_main-medium mb-8']"]
    ORDER_NUMBER = [By.XPATH, '//p[text()="идентификатор заказа"]/preceding-sibling::h2']
    CLOSE_POPUP_NUMBER_ORDER = [By.XPATH, '//*[contains(@class, "Modal_modal__close_modified")]']
    CONTAINER = [By.XPATH, '//a[@class="OrderHistory_link__1iNby"]']
    ORDER_ITEM = [By.XPATH, '//li[@class="text text_type_digits-default mb-2"]']
    ALL_ORDERS_COUNT = [By.XPATH, '//p[contains(@class, "OrderFeed_number")]']
    COUNT_ORDERS_TODAY = [By.XPATH, '//*[text() = "Выполнено за сегодня:"]/following::*[@class][1]']
    IN_PROGRESS = [By.XPATH, '//ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/child::li']
