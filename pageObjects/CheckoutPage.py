from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']")


    def getproducts(self):
        return self.driver.find_elements(*CheckoutPage.products)