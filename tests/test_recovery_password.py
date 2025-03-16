import allure
from pages.password_page import PasswordPage
from urls import Urls
import pytest

class TestRecoveryPassword:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_button_password_recovery(self, driver):
        test = PasswordPage(driver)
        test.lk_click()
        test.recovery_password_click()
        assert driver.current_url == Urls.RECOVERY_PAGE

    @allure.title('Переход на страницу ввода нового пароля')
    def test_enter_mail_click_restore_button(self, driver):
        test = PasswordPage(driver)
        test.lk_click()
        test.recovery_password_click()
        test.email_input()
        test.click_recovery_button()
        test.wait_save_button()
        assert driver.current_url == Urls.RESET_PAGE

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным')
    def test_click_button_invisibility_button(self, driver):
        test = PasswordPage(driver)
        test.lk_click()
        test.recovery_password_click()
        test.email_input()
        test.click_recovery_button()
        test.wait_save_button()
        test.set_new_password()
        test.click_visibility_icon()
        assert test.check_visibility is not None

