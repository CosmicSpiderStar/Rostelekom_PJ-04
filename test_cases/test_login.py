import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.Login_Page_Web import LoginPage
from utilities.read_properties import ReadConfig


class TestLogin:
    # Получаем данные конфигурации
    url_elk_web = ReadConfig.get_url_elk_web()
    url_online_web = ReadConfig.get_url_online_web()
    url_smarthome = ReadConfig.get_url_smarthome()
    valid_email = ReadConfig.get_valid_email()
    invalid_email = ReadConfig.get_invalid_email()
    password = ReadConfig.get_password()
    invalid_password = ReadConfig.get_invalid_password()
    valid_login = ReadConfig.get_invalid_login()
    invalid_login = ReadConfig.get_invalid_login()
    valid_phone = ReadConfig.get_valid_phone()
    invalid_phone = ReadConfig.get_invalid_phone()

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

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, login_page.redirect))
        )

        login_page.click_redirect()

        actual_page_title = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[@class='app-container__title']"))
        ).text

        assert actual_page_title == 'Вход и безопасность'

    def test_online_web_login_with_invalid_email_and_invalid_password(self, driver):
        driver.get(self.url_online_web)
        login_page = LoginPage(driver)

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, login_page.textbox_username_id_02))
        )
        login_page.enter_username_02(self.invalid_email)

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, login_page.textbox_password_id))
        )
        login_page.enter_password(self.invalid_password)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, login_page.btn_login_id))
        )
        login_page.click_login_02()

        error_message = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, "form-error-message"))
        )
        error_message = error_message.text
        assert error_message == 'Неверный логин или пароль'

    def test_online_web_login_with_valid_email_and_invalid_password(self, driver):
        driver.get(self.url_online_web)
        login_page = LoginPage(driver)

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, login_page.textbox_username_id_02))
        )
        login_page.enter_username_02(self.valid_email)

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, login_page.textbox_password_id))
        )
        login_page.enter_password(self.invalid_password)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, login_page.btn_login_id))
        )
        login_page.click_login_02()

        error_message = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, "form-error-message"))
        )
        error_message = error_message.text
        assert error_message == 'Неверный логин или пароль'

    def test_online_web_login_with_valid_phone_and_valid_password(self, driver):
        driver.get(self.url_online_web)
        login_page = LoginPage(driver)

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, login_page.textbox_username_id_02))
        )
        login_page.enter_username_02(self.valid_phone)

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, login_page.textbox_password_id))
        )
        login_page.enter_password(self.password)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, login_page.btn_login_id))
        )
        login_page.click_login_02()

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, login_page.redirect))
        )

        login_page.click_redirect()

        actual_page_title = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[@class='app-container__title']"))
        ).text

        assert actual_page_title == 'Вход и безопасность'

    def test_online_web_login_with_invalid_phone_and_invalid_password(self, driver):
        driver.get(self.url_online_web)
        login_page = LoginPage(driver)

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, login_page.textbox_username_id_02))
        )
        login_page.enter_username_02(self.invalid_phone)

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, login_page.textbox_password_id))
        )
        login_page.enter_password(self.invalid_password)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, login_page.btn_login_id))
        )
        login_page.click_login_02()

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, login_page.redirect))
        )

        login_page.click_redirect()

        actual_page_title = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[@class='app-container__title']"))
        ).text

        assert actual_page_title == 'Вход и безопасность'

    def test_online_web_login_with_valid_phone_and_invalid_password(self, driver):
        driver.get(self.url_online_web)
        login_page = LoginPage(driver)

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, login_page.textbox_username_id_02))
        )
        login_page.enter_username_02(self.valid_phone)

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, login_page.textbox_password_id))
        )
        login_page.enter_password(self.invalid_password)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, login_page.btn_login_id))
        )
        login_page.click_login_02()

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, login_page.redirect))
        )

        login_page.click_redirect()

        error_message = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, "form-error-message"))
        )
        error_message = error_message.text
        assert error_message == 'Неверный логин или пароль'

    def test_online_web_login_with_valid_login_and_valid_password(self, driver):
        driver.get(self.url_online_web)
        login_page = LoginPage(driver)

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, login_page.textbox_username_id_02))
        )
        login_page.enter_username_02(self.valid_login)

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, login_page.textbox_password_id))
        )
        login_page.enter_password(self.password)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, login_page.btn_login_id))
        )
        login_page.click_login_02()

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, login_page.redirect))
        )

        login_page.click_redirect()

        actual_page_title = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[@class='app-container__title']"))
        ).text

        assert actual_page_title == 'Вход и безопасность'

    def test_online_web_login_with_invalid_login_and_invalid_password(self, driver):
        driver.get(self.url_online_web)
        login_page = LoginPage(driver)

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, login_page.textbox_username_id_02))
        )
        login_page.enter_username_02(self.invalid_login)

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, login_page.textbox_password_id))
        )
        login_page.enter_password(self.invalid_password)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, login_page.btn_login_id))
        )
        login_page.click_login_02()

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, login_page.redirect))
        )

        login_page.click_redirect()

        error_message = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, "form-error-message"))
        )
        error_message = error_message.text
        assert error_message == 'Неверный логин или пароль'

    def test_online_web_login_with_valid_login_and_invalid_password(self, driver):
        driver.get(self.url_online_web)
        login_page = LoginPage(driver)

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, login_page.textbox_username_id_02))
        )
        login_page.enter_username_02(self.valid_login)

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, login_page.textbox_password_id))
        )
        login_page.enter_password(self.invalid_password)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, login_page.btn_login_id))
        )
        login_page.click_login_02()

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, login_page.redirect))
        )

        login_page.click_redirect()

        error_message = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, "form-error-message"))
        )
        error_message = error_message.text
        assert error_message == 'Неверный логин или пароль'

    def test_online_web_login_error_message_with_empty_fields_btn_tab_phone(self, driver):
        driver.get(self.url_online_web)
        login_page = LoginPage(driver)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, login_page.btn_tab_phone))
        )
        login_page.click_btn_tab_phone()

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, login_page.btn_login_id))
        )
        login_page.click_login_02()

        eror_message_empty_field = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, 'username-meta'))
        )
        eror_message_empty_field_text = eror_message_empty_field.text
        assert eror_message_empty_field_text == 'Введите номер телефона'

    def test_online_web_login_error_message_with_empty_fields_btn_tab_email(self, driver):
        driver.get(self.url_online_web)
        login_page = LoginPage(driver)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, login_page.btn_tab_email))
        )
        login_page.click_btn_tab_email()

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, login_page.btn_login_id))
        )
        login_page.click_login_02()

        eror_message_empty_field = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, 'username-meta'))
        )
        eror_message_empty_field_text = eror_message_empty_field.text
        assert eror_message_empty_field_text == 'Введите адрес, указанный при регистрации'

    def test_online_web_login_error_message_with_empty_fields_btn_tab_login(self, driver):
        driver.get(self.url_online_web)
        login_page = LoginPage(driver)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, login_page.btn_tab_login))
        )
        login_page.click_btn_tab_login()

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, login_page.btn_login_id))
        )
        login_page.click_login_02()

        eror_message_empty_field = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, 'username-meta'))
        )
        eror_message_empty_field_text = eror_message_empty_field.text
        assert eror_message_empty_field_text == 'Введите логин, указанный при регистрации'

    def test_valid_email_login_with_password_from_elk_web(self, driver):
        driver.get(self.url_elk_web)
        login_page = LoginPage(driver)

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, login_page.textbox_username_id_01))
        )
        login_page.enter_username_01(self.valid_email)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, login_page.btn_login_xpath))
        )
        login_page.click_login_01()

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, login_page.textbox_username_id_02))
        )
        login_page.enter_username_02(self.valid_email)

        # Ожидание ввода пароля
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, login_page.textbox_password_id))
        )
        login_page.enter_password(self.password)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, login_page.btn_login_id))
        )
        login_page.click_login_02()

        actual_page_title = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='StyledHeaderTopPartMenuItemLk-kHgfwO lfjrSy']"))
        ).text

        assert actual_page_title == "Личный кабинет"

    def test_valid_phone_login_with_password_from_elk_web(self, driver):
        driver.get(self.url_elk_web)
        login_page = LoginPage(driver)

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, login_page.textbox_username_id_01))
        )
        login_page.enter_username_01(self.valid_phone)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, login_page.btn_login_xpath))
        )
        login_page.click_login_01()

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, login_page.textbox_username_id_02))
        )
        login_page.enter_username_02(self.valid_phone)

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, login_page.textbox_password_id))
        )
        login_page.enter_password(self.password)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, login_page.btn_login_id))
        )
        login_page.click_login_02()

        actual_page_title = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='StyledHeaderTopPartMenuItemLk-kHgfwO lfjrSy']"))
        ).text

        assert actual_page_title == "Личный кабинет"

    def test_valid_phone_with_valid_password_from_smarthome(self, driver):
        driver.get(self.url_smarthome)
        login_page = LoginPage(driver)

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, login_page.textbox_user_smarthome_01))
        )
        login_page.enter_username_01_smarthome(self.valid_phone)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, login_page.btn_login_xpath))
        )
        login_page.click_btn_smarthome_auth()

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, login_page.textbox_username_id_02))
        )
        login_page.enter_username_02(self.valid_phone)

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, login_page.textbox_password_id))
        )
        login_page.enter_password(self.password)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, login_page.btn_login_id))
        )
        login_page.click_login_02()

        actual_page_title = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[2]/main[1]/div[1]/header[1]/p[1]'))
        ).text

        assert actual_page_title == "Создание нового аккаунта"
