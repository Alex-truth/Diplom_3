import allure
from selenium.common.exceptions import ElementClickInterceptedException

from data import email, password
from locators import LocatorsProfilePage
from pages.base_page import BasePage


class ProfilePage(BasePage):

    @allure.title('Нажимаем на кнопку ЛК')
    def click_lk(self):
        try:
            self.click_element(LocatorsProfilePage.LK_BUTTON)
        except ElementClickInterceptedException:
            lk_button = self.driver.find_element(*LocatorsProfilePage.LK_BUTTON)
            self.driver.execute_script("arguments[0].click();", lk_button)

    @allure.title('Вводим логин')
    def set_login(self):
        self.send_keys_to_input(LocatorsProfilePage.MAIL_INPUT, email)

    @allure.title('Вводим пароль')
    def set_password(self):
        self.send_keys_to_input(LocatorsProfilePage.PASSWORD_INPUT, password)

    @allure.title('Клик по кнопке "Войти')
    def click_enter_button(self):
        self.click_element(LocatorsProfilePage.BUTTON_ENTER)

    @allure.title('Ожидаем загрузку страницы профиля')
    def wait_account_page(self):
        self.wait_to_clickable(LocatorsProfilePage.BUTTON_PROFILE)

    @allure.title('Клик по Истории заказов')
    def click_order_history(self):
        try:
            self.click_element(LocatorsProfilePage.ORDER_HISTORY)
        except ElementClickInterceptedException:
            order_history_element = self.driver.find_element(*LocatorsProfilePage.ORDER_HISTORY)
            self.driver.execute_script("arguments[0].click();", order_history_element)

    @allure.title('Клик по кнопке Выход')
    def click_exit_button(self):
        try:
            self.click_element(LocatorsProfilePage.EXIT_BUTTON)
        except ElementClickInterceptedException:
            exit_button_element = self.driver.find_element(*LocatorsProfilePage.EXIT_BUTTON)
            self.driver.execute_script("arguments[0].click();", exit_button_element)

    @allure.title('Ожидание загрузки страницы при выходе')
    def wait_logout_page(self):
        self.wait_to_clickable(LocatorsProfilePage.BUTTON_ENTER)