import allure
from data import email, password
from locators import LocatorsProfilePage
from pages.base_page import BasePage


class ProfilePage(BasePage):

    @allure.title('Нажимаем на кнопку ЛК')
    def click_lk(self):
        self.click_element(LocatorsProfilePage.LK_BUTTON)

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
        self.click_element(LocatorsProfilePage.ORDER_HISTORY)

    @allure.title('Клик по кнопке Выход')
    def click_exit_button(self):
        self.click_element(LocatorsProfilePage.EXIT_BUTTON)

    @allure.title('Ожидание загрузки страницы при выходе')
    def wait_logout_page(self):
        self.wait_to_clickable(LocatorsProfilePage.BUTTON_ENTER)

    @allure.step('Получаем текущую страницу')
    def get_current_url(self):
        return self.driver.current_url