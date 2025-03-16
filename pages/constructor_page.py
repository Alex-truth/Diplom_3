import allure
from selenium.common.exceptions import ElementClickInterceptedException
from locators import LocatorsConstructorPage
from pages.base_page import BasePage
from data import email, password




class ConstructorPage(BasePage):

    @allure.step('Клик по кнопке "Войти в аккаунт"')
    def click_auth_button(self):
        try:
            self.click_element(LocatorsConstructorPage.BUTTON_AUTH_ACCOUNT)
        except ElementClickInterceptedException:
            element = self.driver.find_element(*LocatorsConstructorPage.BUTTON_AUTH_ACCOUNT)
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Клик по кнопке "Конструктор"')
    def click_constructor_button(self):
        try:
            self.click_element(LocatorsConstructorPage.CONSTRUCTOR_BUTTON)
        except ElementClickInterceptedException:
            element = self.driver.find_element(*LocatorsConstructorPage.CONSTRUCTOR_BUTTON)
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Переход по клику на «Лента заказов»')
    def click_switch_order_feed(self):
        try:
            self.click_element(LocatorsConstructorPage.ORDER_FEED_BUTTON)
        except ElementClickInterceptedException:
            element = self.driver.find_element(*LocatorsConstructorPage.ORDER_FEED_BUTTON)
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Кликаем по ингридиенту "Флюоресцентная булка R2-D3"')
    def click_ingredient_fluorescent_bun(self):
        try:
            self.click_element(LocatorsConstructorPage.FLUORESCENT_BUN)
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();",
                                       self.driver.find_element(*LocatorsConstructorPage.FLUORESCENT_BUN))

    @allure.step('Находим элемент Детали интредиента')
    def get_ingredient_window(self):
        self.wait_to_visibility(LocatorsConstructorPage.INGREDIENT_WINDOW)
        return self.get_element(LocatorsConstructorPage.INGREDIENT_WINDOW)

    @allure.step('Кликаем на крестик, закрывая окно "Детали ингредиента"')
    def click_close_ingredient_window(self):
        try:
            self.click_element(LocatorsConstructorPage.EXIT_INGREDIENT_WINDOW)
        except ElementClickInterceptedException:
            element = self.driver.find_element(*LocatorsConstructorPage.EXIT_INGREDIENT_WINDOW)
            self.driver.execute_script("arguments[0].click();", element)

        self.wait_to_invisibility(LocatorsConstructorPage.INGREDIENT_WINDOW)

    @allure.step('Получаем текущий счётчик ингредиента')
    def get_ingredient_counter(self):
        return int(self.read_text(LocatorsConstructorPage.INGREDIENT_COUNTER))

    @allure.step('Перетаскиваем ингредиент "Флюоресцентная булка" в заказ')
    def drag_and_drop_ingredient_fluorescent_bun_to_order(self):
        self.drag_and_drop(LocatorsConstructorPage.FLUORESCENT_BUN, LocatorsConstructorPage.INGREDIENT_BASKET)


    @allure.step('Клик по кнопке "Оформить заказ')
    def click_on_checkout_button(self):
        try:
            self.click_element(LocatorsConstructorPage.CHECKOUT_BUTTON)
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();",
                                       self.driver.find_element(*LocatorsConstructorPage.CHECKOUT_BUTTON))

    @allure.step('Логиним пользователя')
    def login(self):
        try:
            self.click_element(LocatorsConstructorPage.BUTTON_AUTH_ACCOUNT)
        except Exception as e:
            print(f"Ошибка при клике по кнопке 'Авторизация' обычным способом: {e}")
            button = self.driver.find_element(*LocatorsConstructorPage.BUTTON_AUTH_ACCOUNT)
            self.driver.execute_script("arguments[0].click();", button)

        self.send_keys_to_input(LocatorsConstructorPage.MAIL_INPUT, email)
        self.send_keys_to_input(LocatorsConstructorPage.PASSWORD_INPUT, password)

        try:
            self.click_element(LocatorsConstructorPage.BUTTON_ENTER)
        except Exception as e:
            print(f"Ошибка при клике по кнопке 'Войти' обычным способом: {e}")
            button = self.driver.find_element(*LocatorsConstructorPage.BUTTON_ENTER)
            self.driver.execute_script("arguments[0].click();", button)


    @allure.step('Заказ начали готовить')
    def order_is_being_prepared(self):
        self.wait_to_visibility(LocatorsConstructorPage.ORDER_PREPARED)
        return self.get_element(LocatorsConstructorPage.ORDER_PREPARED)