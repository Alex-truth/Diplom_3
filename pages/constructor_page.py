import allure
from locators import LocatorsConstructorPage
from pages.base_page import BasePage
from data import email, password


class ConstructorPage(BasePage):

    @allure.step('Клик по кнопке "Войти в аккаунт"')
    def click_auth_button(self):
        self.click_element(LocatorsConstructorPage.BUTTON_AUTH_ACCOUNT)

    @allure.step('Клик по кнопке "Конструктор"')
    def click_constructor_button(self):
        self.click_element(LocatorsConstructorPage.CONSTRUCTOR_BUTTON)

    @allure.step('Переход по клику на «Лента заказов»')
    def click_switch_order_feed(self):
        self.click_element(LocatorsConstructorPage.ORDER_FEED_BUTTON)

    @allure.step('Кликаем по ингридиенту "Флюоресцентная булка R2-D3"')
    def click_ingredient_fluorescent_bun(self):
        self.click_element(LocatorsConstructorPage.FLUORESCENT_BUN)

    @allure.step('Находим элемент Детали интредиента')
    def get_ingredient_window(self):
        self.wait_to_visibility(LocatorsConstructorPage.INGREDIENT_WINDOW)
        return self.get_element(LocatorsConstructorPage.INGREDIENT_WINDOW)

    @allure.step('Кликаем на крестик, закрывая окно "Детали ингредиента"')
    def click_close_ingredient_window(self):
        self.click_element(LocatorsConstructorPage.EXIT_INGREDIENT_WINDOW)
        self.wait_to_invisibility(LocatorsConstructorPage.INGREDIENT_WINDOW)

    @allure.step('Получаем текущий счётчик ингредиента')
    def get_ingredient_counter(self):
        return int(self.read_text(LocatorsConstructorPage.INGREDIENT_COUNTER))

    @allure.step('Перетаскиваем ингредиент "Флюоресцентная булка" в заказ')
    def drag_and_drop_ingredient_fluorescent_bun_to_order(self):
        self.drag_and_drop(LocatorsConstructorPage.FLUORESCENT_BUN, LocatorsConstructorPage.INGREDIENT_BASKET)


    @allure.step('Клик по кнопке "Оформить заказ')
    def click_on_checkout_button(self):
        self.click_element(LocatorsConstructorPage.CHECKOUT_BUTTON)

    @allure.step('Логиним пользователя')
    def login(self):
        self.click_element(LocatorsConstructorPage.BUTTON_AUTH_ACCOUNT)
        self.send_keys_to_input(LocatorsConstructorPage.MAIL_INPUT, email)
        self.send_keys_to_input(LocatorsConstructorPage.PASSWORD_INPUT, password)
        self.click_element(LocatorsConstructorPage.BUTTON_ENTER)


    @allure.step('Заказ начали готовить')
    def order_is_being_prepared(self):
        self.wait_to_visibility(LocatorsConstructorPage.ORDER_PREPARED)
        return self.get_element(LocatorsConstructorPage.ORDER_PREPARED)

    @allure.step('Получаем текущую страницу')
    def get_current_url(self):
        return self.driver.current_url