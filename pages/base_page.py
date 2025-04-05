from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    @allure.step("Ожидаем загрузки элемента")
    def wait_to_visibility(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидаем, что элемент станет кликабельным')
    def wait_to_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Принудительный клик по элементу")
    def force_click(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Клик по элементу')
    def click_element(self, locator):
        self.wait_to_clickable(locator)
        try:
            self.driver.find_element(*locator).click()
        except ElementClickInterceptedException:
            self.force_click(locator)

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
        self.wait.until(EC.invisibility_of_element_located(locator))

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
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step('Получить текущий url')
    def current_url(self):
        return self.driver.current_url

    @allure.step('Ожидаем обновление текста элемента')
    def wait_for_text_update(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))
        self.wait.until(lambda driver: self.read_text(locator).isdigit() and self.read_text(locator) != "9999")
        return self.read_text(locator)