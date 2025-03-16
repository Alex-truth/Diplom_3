import allure
from locators import LocatorsPwdPage
from data import email, password
from pages.base_page import BasePage
from selenium.common.exceptions import ElementClickInterceptedException


class PasswordPage(BasePage):

    @allure.step('Клик по кнопке "Личный кабинет"')
    def lk_click(self):
        self.click_element(LocatorsPwdPage.LK_BUTTON)

    @allure.step('Клик по кнопке "Восстанавить пароль')
    def recovery_password_click(self):
        self.click_element(LocatorsPwdPage.RECOVERY_PASSWORD)

    @allure.step('Вводим email')
    def email_input(self):
        self.send_keys_to_input(LocatorsPwdPage.MAIL_INPUT, email)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_recovery_button(self):
        self.click_element(LocatorsPwdPage.RESTORE_BUTTON)

    @allure.step('Ожидаем загрузку кнопки "Сохранить"')
    def wait_save_button(self):
        self.wait_to_visibility(LocatorsPwdPage.SAVE_PWD_BUTTON)

    @allure.step('Вводим новый пароль')
    def set_new_password(self):
        self.send_keys_to_input(LocatorsPwdPage.INPUT_NEW_PASSWORD, password)

    @allure.step('Клик по иконке видимости пароля')
    def click_visibility_icon(self):
        self.wait_to_clickable(LocatorsPwdPage.BUTTON_VISIBILITY_PASSWORD)
        try:
            self.click_element(LocatorsPwdPage.BUTTON_VISIBILITY_PASSWORD)
        except ElementClickInterceptedException:
            element = self.driver.find_element(*LocatorsPwdPage.BUTTON_VISIBILITY_PASSWORD)
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Проверка активности скрытия элемента')
    def check_visibility(self):
        self.wait_to_visibility(LocatorsPwdPage.SEARCH_ELEMENT)