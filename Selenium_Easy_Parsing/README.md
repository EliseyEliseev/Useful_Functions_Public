# Класс "Помощник Selenium"
Это класс на Python, который предоставляет набор методов-помощников для использования Selenium WebDriver в автоматизации тестирования веб-приложений.

# Установка
Для использования этого класса необходимо установить Selenium WebDriver. Это можно сделать с помощью команды:
```python
pip install selenium
```
# Использование
Чтобы использовать класс SeleniumHelperClass, необходимо сначала импортировать его и создать экземпляр, передавая в него экземпляр Selenium WebDriver:
```python
from selenium import webdriver
from selenium_helper_class import SeleniumHelperClass

driver = webdriver.Chrome()
helper = SeleniumHelperClass(driver)
```
Затем можно использовать методы-помощники для автоматизации тестирования веб-приложений:
```python
locator = (By.ID, 'my-element')
helper.click(locator)

text_locator = (By.XPATH, '//div[@class="my-class"]')
text = helper.get_text(text_locator)

input_locator = (By.CSS_SELECTOR, 'input[name="my-input"]')
helper.send_keys(input_locator, 'some text')
```

# Методы-помощники
Предоставляются следующие методы-помощники:

* **wait_for_element(locator, timeout=10)**: ожидание появления  элемента на странице
* wait_for_clickable(locator, timeout=10): ожидание, пока элемент станет кликабельным
* **find_element(locator)**: поиск элемента на странице
* **find_elements(locator)**: поиск списка элементов на странице
* **click(locator)**: клик по элементу
* **send_keys(locator, text)**: ввод текста в поле ввода
* **get_text(locator)**: получение текста элемента
* **get_attribute(locator, attribute)**: получение значения  атрибута элемента
* **wait_for_alert(timeout=10)**: ожидание появления всплывающего окна
* **switch_to_frame(locator)**: переключение на iframe
* **switch_to_default_content()**: переключение на основную страницу


# Пример кода
Пример кода который использует мой класс, можно найти [нажав по этому тексту](example_of_using.py)
