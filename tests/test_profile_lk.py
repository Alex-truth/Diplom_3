import allure
import pytest
from pages.profile_page import ProfilePage
from urls import Urls

class TestProfileAccount:

    @allure.title('Переход по клику на «Личный кабинет»')
    def test_switch_lk_button(self, driver):
        test = ProfilePage(driver)
        test.click_lk()
        test.set_login()
        test.set_password()
        test.click_enter_button()
        test.click_lk()
        test.wait_account_page()
        assert driver.current_url == Urls.ACCOUNT_PROFILE

    @allure.title('Переход на вкладку История заказов')
    def test_switch_order_history(self, driver):
        test = ProfilePage(driver)
        test.click_lk()
        test.set_login()
        test.set_password()
        test.click_enter_button()
        test.click_lk()
        test.click_order_history()
        assert driver.current_url == Urls.ORDER_HISTORY

    @allure.title('Выход из аккаунта')
    def test_logout(self, driver):
        test = ProfilePage(driver)
        test.click_lk()
        test.set_login()
        test.set_password()
        test.click_enter_button()
        test.click_lk()
        test.click_exit_button()
        test.wait_logout_page()
        assert driver.current_url == Urls.LOGIN_PAGE
