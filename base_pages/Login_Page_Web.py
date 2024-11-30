from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id_01 = "address"
    textbox_username_id_02 = "username"
    textbox_password_id = "password"
    btn_login_xpath = '//button[@class="rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded rt-btn--outline otp-form__back-login-btn"]'
    btn_login_id = "kc-login"
    redirect = '//a[@class = "rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded reset-form__reset-btn"]'
    btn_tab_phone = 't-btn-tab-phone'
    btn_tab_email = 't-btn-tab-mail'
    btn_tab_login = 't-btn-tab-login'
    btn_smarthome = 'standard_auth_btn'
    textbox_user_smarthome_01 = 'address'

    def __init__(self, driver):
        self.driver = driver

    def enter_username_01(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id_01).send_keys(username)

    def enter_username_02(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id_02).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login_01(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def click_login_02(self):
        self.driver.find_element(By.ID, self.btn_login_id).click()

    def click_redirect(self):
        self.driver.find_element(By.XPATH, self.redirect).click()

    def click_btn_tab_phone(self):
        self.driver.find_element(By.ID, self.btn_tab_phone).click()

    def click_btn_tab_email(self):
        self.driver.find_element(By.ID, self.btn_tab_email).click()

    def click_btn_tab_login(self):
        self.driver.find_element(By.ID, self.btn_tab_login).click()

    def click_btn_smarthome_auth(self):
        self.driver.find_element(By.ID, self.btn_smarthome).click()

    def enter_username_01_smarthome(self, username):
        self.driver.find_element(By.ID, self.textbox_user_smarthome_01).send_keys(username)
