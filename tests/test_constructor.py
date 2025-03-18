import allure
from urls import Urls
from pages.constructor_page import ConstructorPage


class TestConstructor:

    @allure.title('Переход по клику на «Конструктор»')
    def test_click_switch_constructor(self, driver):
        test = ConstructorPage(driver)
        test.click_auth_button()
        test.click_constructor_button()
        assert test.get_current_url() == Urls.MAIN_PAGE

    @allure.title('Переход по клику на «Лента заказов»')
    def test_click_order_feed(self, driver):
        test = ConstructorPage(driver)
        test.click_auth_button()
        test.click_switch_order_feed()
        assert test.get_current_url() == Urls.ORDER_FEED

    @allure.title('При клике на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient_window_apper(self, driver):
        test = ConstructorPage(driver)
        test.click_ingredient_fluorescent_bun()
        element = test.get_ingredient_window()
        assert element.is_displayed()

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_ingredient_window(self, driver):
        test = ConstructorPage(driver)
        test.click_ingredient_fluorescent_bun()
        element = test.get_ingredient_window()
        test.click_close_ingredient_window()
        assert not element.is_displayed()

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_ingredient_counter_increases(self, driver):
        test = ConstructorPage(driver)
        initial_count = test.get_ingredient_counter()
        test.drag_and_drop_ingredient_fluorescent_bun_to_order()
        new_count = test.get_ingredient_counter()
        assert new_count == initial_count + 2

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_logged_user_can_place_order(self, driver):
        test = ConstructorPage(driver)
        test.click_auth_button()
        test.login()
        test.drag_and_drop_ingredient_fluorescent_bun_to_order()
        test.click_on_checkout_button()
        element = test.order_is_being_prepared()
        assert element.is_displayed()



