import pytest
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_form_submission(self, get_data):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info('first name is: ' + get_data['firstname'])
        homepage.get_name().send_keys(get_data['firstname'])
        homepage.get_mail().send_keys(get_data['lastname'])
        homepage.get_password().send_keys(get_data['password'])
        homepage.get_id().click()
        self.select_option_by_index(homepage.get_gender(), get_data['genderindex'])
        homepage.get_submit().click()

        message = homepage.get_success_message().text

        print(message)
        assert 'Success' in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.get_test_data('Testcase2'))
    def get_data(self, request):
        return request.param
