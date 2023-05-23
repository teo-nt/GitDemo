from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, 'Shop')
    mail = (By.NAME, 'email')
    name = (By.CSS_SELECTOR, "input[name='name']")
    password = (By.ID, 'exampleInputPassword1')
    ID = (By.ID, 'exampleCheck1')
    gender = (By.ID, 'exampleFormControlSelect1')
    submit = (By.XPATH, '//input[@type="submit"]')
    success_message = (By.CLASS_NAME, 'alert-success')

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)

    def get_mail(self):
        return self.driver.find_element(*HomePage.mail)

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_password(self):
        return self.driver.find_element(*HomePage.password)

    def get_id(self):
        return self.driver.find_element(*HomePage.ID)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def get_submit(self):
        return self.driver.find_element(*HomePage.submit)

    def get_success_message(self):
        return self.driver.find_element(*HomePage.success_message)
