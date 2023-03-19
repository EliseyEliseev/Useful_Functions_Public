from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumHelperClass:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        """
        Ожидание появления элемента на странице.
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def wait_for_clickable(self, locator, timeout=10):
        """
        Ожидание, пока элемент станет кликабельным.
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    def find_element(self, locator):
        """
        Поиск элемента на странице.
        """
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        """
        Поиск списка элементов на странице.
        """
        return self.driver.find_elements(*locator)

    def click(self, locator):
        """
        Клик по элементу.
        """
        element = self.wait_for_clickable(locator)
        element.click()

    def send_keys(self, locator, text):
        """
        Ввод текста в поле ввода.
        """
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """
        Получение текста элемента.
        """
        element = self.wait_for_element(locator)
        return element.text

    def get_attribute(self, locator, attribute):
        """
        Получение значения атрибута элемента.
        """
        element = self.wait_for_element(locator)
        return element.get_attribute(attribute)

    def wait_for_alert(self, timeout=10):
        """
        Ожидание появления всплывающего окна.
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.alert_is_present())

    def switch_to_frame(self, locator):
        """
        Переключение на iframe.
        """
        frame = self.wait_for_element(locator)
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        """
        Переключение на основную страницу.
        """
        self.driver.switch_to.default_content()
