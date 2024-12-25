# Проект тестов авторизации

## **Описание проекта**

Этот проект содержит тесты для проверки авторизации пользователей на различных веб-платформах. Тесты написаны на Python с использованием библиотек `pytest` и `selenium`. Сценарии тестируют корректность обработки логина и пароля, включая поддержку различных типов учетных данных (email, телефон, логин) в веб-приложениях.

## **Структура проекта**

- **`TestLogin`**: Класс, содержащий тесты для проверки функциональности авторизации.
- **`base_pages/Login_Page_Web.py`**: Базовый класс страницы авторизации.
- **`utilities/read_properties.py`**: Утилита для чтения конфигурационных данных.
- **Конфигурационные файлы**: Содержат тестовые данные, такие как URL-адреса, логины и пароли.

## **Предварительные требования**

Перед запуском тестов убедитесь, что у вас установлено следующее:

- **Python 3.8 или выше**
- Необходимые библиотеки:
  - `pytest`
  - `selenium`
- Веб-драйвер (например, ChromeDriver) для браузера, используемого в тестах.

## **Установка**

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/CosmicSpiderStar/Rostelekom_PJ-04
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## **Конфигурация**

Укажите данные (например, URL-адреса, учетные данные) в файле конфигурации, используемом модулем `utilities/read_properties.py`.

## **Запуск тестов**

### Запуск всех тестов
Выполните все тесты с помощью команды:
```bash
pytest
```

### Запуск конкретного теста
Запустите конкретный тест по его имени:
```bash
pytest -k "test_name"
```

## **Описание тестов**

### Тесты авторизации с валидными данными
- **Цель**: Проверить авторизацию через email, номер телефона или логин с правильным паролем.
- **Ожидаемый результат**: Успешная авторизация перенаправляет пользователя на защищенную страницу.

### Тесты авторизации с невалидными данными
- **Цель**: Проверить авторизацию с неправильным email, номером телефона, логином или паролем.
- **Ожидаемый результат**: Отображение соответствующих сообщений об ошибках.

### Проверка пустых полей
- **Цель**: Проверить поля логина и пароля с пустыми значениями.
- **Ожидаемый результат**: Отображение сообщений о необходимости заполнения полей.

## **Пример теста**

```python
def test_online_web_login_with_valid_email_and_valid_password(self, driver):
    driver.get(self.url_online_web)
    login_page = LoginPage(driver)

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.ID, login_page.textbox_username_id_02))
    )
    login_page.enter_username_02(self.valid_email)

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.ID, login_page.textbox_password_id))
    )
    login_page.enter_password(self.password)

    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, login_page.btn_login_id))
    )
    login_page.click_login_02()

    actual_page_title = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[@class='app-container__title']"))
    ).text

    assert actual_page_title == 'Вход и безопасность'
```



