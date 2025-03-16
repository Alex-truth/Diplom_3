import allure
from data import email, password
from locators import LocatorsOrderPage, LocatorsConstructorPage
from pages.base_page import BasePage
from selenium.common.exceptions import ElementClickInterceptedException

class OrderFeed(BasePage):

    @allure.step('Переходим в ленту заказов')
    def click_switch_order_feed(self):
        try:
            self.click_element(LocatorsConstructorPage.ORDER_FEED_BUTTON)
        except ElementClickInterceptedException:
            element = self.driver.find_element(*LocatorsConstructorPage.ORDER_FEED_BUTTON)
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Кликаем на последний заказ')
    def click_last_order(self):
        self.click_element(LocatorsOrderPage.LAST_ORDER)

    @allure.step('Наличие состава')
    def order_details(self):
        self.wait_to_visibility(LocatorsOrderPage.STRUCTURE)
        return self.get_element(LocatorsOrderPage.STRUCTURE)

    @allure.step('Логиним пользователя')
    def login(self):
        try:
            self.click_element(LocatorsConstructorPage.BUTTON_AUTH_ACCOUNT)
        except ElementClickInterceptedException:
            button = self.driver.find_element(*LocatorsConstructorPage.BUTTON_AUTH_ACCOUNT)
            self.driver.execute_script("arguments[0].click();", button)

        self.send_keys_to_input(LocatorsConstructorPage.MAIL_INPUT, email)
        self.send_keys_to_input(LocatorsConstructorPage.PASSWORD_INPUT, password)

        try:
            self.click_element(LocatorsConstructorPage.BUTTON_ENTER)
        except ElementClickInterceptedException:
            button = self.driver.find_element(*LocatorsConstructorPage.BUTTON_ENTER)
            self.driver.execute_script("arguments[0].click();", button)

    @allure.step('Перетаскиваем ингредиент "Флюоресцентная булка" в заказ')
    def drag_and_drop_ingredient_fluorescent_bun_to_order(self):
        self.drag_and_drop(LocatorsConstructorPage.FLUORESCENT_BUN, LocatorsConstructorPage.INGREDIENT_BASKET)

    @allure.step('Клик по кнопке "Оформить заказ')
    def click_on_checkout_button(self):
        self.wait_to_clickable(LocatorsConstructorPage.CHECKOUT_BUTTON)
        try:
            self.click_element(LocatorsConstructorPage.CHECKOUT_BUTTON)
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();",
                                       self.driver.find_element(*LocatorsConstructorPage.CHECKOUT_BUTTON))


    @allure.step('Получаем номер заказа')
    def get_order_number(self):
        self.wait_to_visibility(LocatorsOrderPage.ORDER_NUMBER)
        return self.read_text(LocatorsOrderPage.ORDER_NUMBER)

    @allure.step('Закрываем окно с номером заказа')
    def close_popup_order_number(self):
        self.wait_to_clickable(LocatorsOrderPage.CLOSE_POPUP_NUMBER_ORDER)
        self.click_element(LocatorsOrderPage.CLOSE_POPUP_NUMBER_ORDER)

    def get_orders_numbers(self):
        self.wait_to_visibility(LocatorsOrderPage.CONTAINER)
        order_elements = self.get_elements(LocatorsOrderPage.ORDER_ITEM)
        order_numbers = []
        for order in order_elements:
            order_numbers.append(order.text)
        return order_numbers

    @allure.step('Получаем количество оформленных заказов за все время')
    def get_all_orders(self):
        self.wait_to_visibility(LocatorsOrderPage.ALL_ORDERS_COUNT)
        return self.read_text(LocatorsOrderPage.ALL_ORDERS_COUNT)

    @allure.step('Переходим в раздел  "Конструктор"')
    def click_constructor_button(self):
        self.wait_to_clickable(LocatorsConstructorPage.CONSTRUCTOR_BUTTON)
        try:
            self.click_element(LocatorsConstructorPage.CONSTRUCTOR_BUTTON)
        except ElementClickInterceptedException:
            element = self.driver.find_element(*LocatorsConstructorPage.CONSTRUCTOR_BUTTON)
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Количество заказов за день')
    def get_count_today(self):
        self.wait_to_visibility(LocatorsOrderPage.COUNT_ORDERS_TODAY)
        return self.read_text(LocatorsOrderPage.COUNT_ORDERS_TODAY)

    @allure.step('Получаем номер заказа в разделе "В работе"')
    def get_order_number_in_progress(self):
        self.wait_to_visibility(LocatorsOrderPage.IN_PROGRESS)
        return self.read_text(LocatorsOrderPage.IN_PROGRESS)