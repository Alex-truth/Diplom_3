from selenium.webdriver.common.action_chains import ActionChains
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидаем загрузки элемента")
    def wait_to_visibility(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидаем, что элемент станет кликабельным')
    def wait_to_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    @allure.step('Клик по элементу')
    def click_element(self, locator):
        self.wait_to_clickable(locator)
        self.driver.find_element(*locator).click()

    @allure.step("Читать текст элемента")
    def read_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Ввод данных')
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Находим элемент на странице')
    def get_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Ожидаем исчезновения элемента")
    def wait_to_invisibility(self, locator):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))

    @allure.step('Перетаскиваем элемент в целевую зону')
    def drag_and_drop(self, source_locator, target_locator):
        source_element = self.get_element(source_locator)
        target_element = self.get_element(target_locator)

        if self.driver.name.lower() == 'firefox':
            self.driver.execute_script("""
                function createEvent(typeOfEvent) {
                    var event = document.createEvent("CustomEvent");
                    event.initCustomEvent(typeOfEvent, true, true, null);
                    event.dataTransfer = {
                        data: {},
                        setData: function(key, value) {
                            this.data[key] = value;
                        },
                        getData: function(key) {
                            return this.data[key];
                        }
                    };
                    return event;
                }

                var event = createEvent('dragstart');
                arguments[0].dispatchEvent(event);

                var dropEvent = createEvent('drop');
                arguments[1].dispatchEvent(dropEvent);
            """, source_element, target_element)
        else:
            action = ActionChains(self.driver)
            action.click_and_hold(source_element).move_to_element(target_element).release().perform()

    @allure.step('Возвращает все элементы, соответствующие локатору')
    def get_elements(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)