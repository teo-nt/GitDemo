from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures('setup')
class Testone(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.shopItems().click()

        checkoutPage = CheckoutPage(self.driver)
        products = checkoutPage.getproducts()
        log.info('getting all the card titles')
        for prod in products:
            product_name = prod.find_element(By.XPATH, "div/h4/a").text
            log.info(product_name)
            if product_name == 'Blackberry':
                prod.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()
        self.driver.find_element(By.CSS_SELECTOR, '.btn-success').click()
        log.info('entering country name as gr')
        self.driver.find_element(By.ID, 'country').send_keys('gr')
        self.verifyLinkpresence('Greece')
        self.driver.find_element(By.LINK_TEXT, 'Greece').click()
        self.driver.find_element(By.XPATH, '//div[@class="checkbox checkbox-primary"]').click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        text = self.driver.find_element(By.CSS_SELECTOR, '.alert-success').text

        log.info(f'Text received from application is: {text[2:]}')
        assert 'Success! Thank you!' in text
