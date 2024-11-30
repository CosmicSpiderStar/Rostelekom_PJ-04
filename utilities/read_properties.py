import configparser

config = configparser.RawConfigParser()
config.read("C:/Users/Ира/PycharmProjects/tests_rostelekom/configurations/config.ini")


class ReadConfig:
    @staticmethod
    def get_url_elk_web():
        return config.get('login info', 'url_elk_web')

    @staticmethod
    def get_url_online_web():
        return config.get('login info', 'url_online_web')

    @staticmethod
    def get_url_smarthome():
        return config.get('login info', 'url_smarthome')

    @staticmethod
    def get_valid_email():
        return config.get('login info', 'valid_email')

    @staticmethod
    def get_invalid_email():
        return config.get('login info', 'invalid_email')

    @staticmethod
    def get_password():
        return config.get('login info', 'password')

    @staticmethod
    def get_invalid_password():
        return config.get('login info', 'invalid_password')

    @staticmethod
    def get_valid_login():
        return config.get('login info','valid_login')

    @staticmethod
    def get_invalid_login():
        return config.get('login info','invalid_login')

    @staticmethod
    def get_valid_phone():
        return config.get('login info','valid_phone')

    @staticmethod
    def get_invalid_phone():
        return config.get('login info','invalid_phone')
