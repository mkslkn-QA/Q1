'''
'''
import pytest
from Pages.BaseApp import BaseMethod

@pytest.mark.auth
class AuthTests:
    def test_login(self, browser):
        '''
        '''
        login_page = BaseMethod(browser)
        login_page.go_to_site()

        assert True, ''


        