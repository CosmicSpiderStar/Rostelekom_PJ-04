import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()  # Разворачиваем браузер
    yield driver  # Передаем драйвер в тест
    driver.quit()  # Закрываем браузер после теста
