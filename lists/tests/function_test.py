import pytest
from selenium import webdriver


@pytest.fixture()
def setup(request):
    browser = webdriver.Firefox()
    request.instance.driver = browser
    browser.get('http://localhost:8000')
    yield browser
    browser.close()


class Test:

    @pytest.mark.usefixtures('setup')
    def test_home_page_return_correct_html(self):
        assert 'To-Do' in self.driver.title

