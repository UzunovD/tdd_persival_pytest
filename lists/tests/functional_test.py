import pytest
from selenium import webdriver


@pytest.fixture()
def setup(request):
    driver = webdriver.Firefox()
    request.instance.driver = driver
    driver.get('http://localhost:8000')
    yield driver
    driver.close()


@pytest.mark.usefixtures('setup')
class Test:
    def test_can_make_task(self):
        assert 'To-Do' in self.driver.title


