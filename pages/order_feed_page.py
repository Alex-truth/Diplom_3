import allure
from data import email, password
from locators import LocatorsOrderPage, LocatorsConstructorPage
from pages.base_page import BasePage


class OrderFeed(BasePage):

    @allure.step('Переходим в ленту заказов')
    def click_switch_order_feed(self):
        self.click_element(LocatorsConstructorPage.ORDER_FEED_BUTTON)


    @allure.step('Кликаем на последний заказ')
    def click_last_order(self):
        self.click_element(LocatorsOrderPage.LAST_ORDER)

    @allure.step('Наличие состава')
    def order_details(self):
        self.wait_to_visibility(LocatorsOrderPage.STRUCTURE)
        return self.get_element(LocatorsOrderPage.STRUCTURE)

    @allure.step('Логиним пользователя')
    def login(self):
        self.click_element(LocatorsConstructorPage.BUTTON_AUTH_ACCOUNT)
        self.send_keys_to_input(LocatorsConstructorPage.MAIL_INPUT, email)
        self.send_keys_to_input(LocatorsConstructorPage.PASSWORD_INPUT, password)
        self.click_element(LocatorsConstructorPage.BUTTON_ENTER)

    @allure.step('Перетаскиваем ингредиент "Флюоресцентная булка" в заказ')
    def drag_and_drop_ingredient_fluorescent_bun_to_order(self):
        self.drag_and_drop(LocatorsConstructorPage.FLUORESCENT_BUN, LocatorsConstructorPage.INGREDIENT_BASKET)

    @allure.step('Клик по кнопке "Оформить заказ')
    def click_on_checkout_button(self):
        self.wait_to_clickable(LocatorsConstructorPage.CHECKOUT_BUTTON)
        self.click_element(LocatorsConstructorPage.CHECKOUT_BUTTON)

    @allure.step('Получаем номер заказа и ждем его обновления')
    def get_order_number(self):
        return self.wait_for_text_update(LocatorsOrderPage.ORDER_NUMBER)

    @allure.step('Закрываем окно с номером заказа')
    def close_popup_order_number(self):
        self.wait_to_clickable(LocatorsOrderPage.CLOSE_POPUP_NUMBER_ORDER)
        self.click_element(LocatorsOrderPage.CLOSE_POPUP_NUMBER_ORDER)

    @allure.step('Получаем список заказов')
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
        self.click_element(LocatorsConstructorPage.CONSTRUCTOR_BUTTON)

    @allure.step('Количество заказов за день')
    def get_count_today(self):
        self.wait_to_visibility(LocatorsOrderPage.COUNT_ORDERS_TODAY)
        return self.read_text(LocatorsOrderPage.COUNT_ORDERS_TODAY)

    @allure.step('Количество заказов за день с ожиданием')
    def new_get_count_today(self):
        return self.wait_for_text_update(LocatorsOrderPage.COUNT_ORDERS_TODAY)


    @allure.step('Получаем номер заказа в разделе "В работе"')
    def get_order_number_in_progress(self):
        return self.wait_for_text_update(LocatorsOrderPage.IN_PROGRESS)