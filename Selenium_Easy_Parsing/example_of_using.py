from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium_helper_class import SeleniumHelperClass

# Создание экземпляра браузера
driver = webdriver.Chrome()

# Создание экземпляра парсера
parser = SeleniumHelperClass(driver)

# Открытие страницы Google
driver.get("https://www.google.com")

# Принятие cookies
cookies_button = parser.wait_for_element((By.XPATH, "/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]"), timeout=1)
cookies_button.click()

# Поиск по слову "Selenium"
search_box = parser.wait_for_element((By.NAME, "q"))
search_box.send_keys("Selenium")
search_box.send_keys(Keys.RETURN)

# Ожидание загрузки страницы с результатами поиска
try:
    parser.wait_for_element((By.XPATH, "//div[@id='search']//a/h3"))
except TimeoutException:
    print("TimeoutException: элемент не найден")
    driver.quit()

# Клик на первую ссылку в результате поиска
links = parser.find_elements((By.XPATH, "//div[@id='search']//a"))
first_link = links[0]
parser.click(first_link)

# Вывод заголовка страницы
print(parser.get_text((By.TAG_NAME, "h1")))

# Закрытие браузера
driver.quit()
