import allure
from pages.order_feed_page import OrderFeed


class TestOrderFeed:

    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_popup_up(self, driver):
        test = OrderFeed(driver)
        test.click_switch_order_feed()
        test.click_last_order()
        element = test.order_details()
        assert element.is_displayed()

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_in_order_feed(self, driver):
        test = OrderFeed(driver)
        test.login()
        test.drag_and_drop_ingredient_fluorescent_bun_to_order()
        test.click_on_checkout_button()
        value = test.get_order_number()
        test.close_popup_order_number()
        test.click_switch_order_feed()
        orders_numbers = test.get_orders_numbers()
        assert '0' + value in orders_numbers

    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_creating_order_counter_completed_all_time_is_incremented(self, driver):
        test = OrderFeed(driver)
        test.login()
        test.click_switch_order_feed()
        count = test.get_all_orders()
        test.click_constructor_button()
        test.drag_and_drop_ingredient_fluorescent_bun_to_order()
        test.click_on_checkout_button()
        test.close_popup_order_number()
        test.click_switch_order_feed()
        new_count = test.get_all_orders()
        assert int(new_count) > int(count)

    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_creating_order_counter_completed_today_is_incremented(self, driver):
        test = OrderFeed(driver)
        test.login()
        test.click_switch_order_feed()
        count = test.get_count_today()
        test.click_constructor_button()
        test.drag_and_drop_ingredient_fluorescent_bun_to_order()
        test.click_on_checkout_button()
        test.close_popup_order_number()
        test.click_switch_order_feed()
        new_count = test.new_get_count_today()
        assert int(new_count) > int(count)

    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_after_create_order_its_number_appears_in_progress(self, driver):
        test = OrderFeed(driver)
        test.login()
        test.drag_and_drop_ingredient_fluorescent_bun_to_order()
        test.click_on_checkout_button()
        count = test.get_order_number()
        test.close_popup_order_number()
        test.click_switch_order_feed()
        new_count = test.get_order_number_in_progress()
        assert '0' + count in new_count