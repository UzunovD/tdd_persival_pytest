import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@pytest.fixture()
def setup(request):
    driver = webdriver.Firefox()
    request.instance.driver = driver
    driver.get('http://localhost:8000')
    yield driver
    driver.close()


@pytest.mark.usefixtures('setup')
class Test:
    def test_can_start_a_list_and_retrieve_it_later(self):
        """Тест: можно начать список и получить его позже"""
        # Эдит слышала про новое онлайн-приложение со списком
        # неотложных дел. Она решает оценить его домашнюю страницу

        # Она видит, что заголовок и шапка страницы говорят о
        # неотложных дел
        assert 'To-Do' in self.driver.title
        headr_text = self.driver.find_element(By.TAG_NAME, 'h1').text
        assert 'To-Do' in headr_text

        # Ей сразу же предлагается ввести элемент списка
        inputbox = self.driver.find_element(By.ID, 'id_new_item')
        assert inputbox.get_attribute('placeholder') == \
                'Enter a to-do item'

        # Она набирвает в текстовом поле "Купить павлиньи перья"
        inputbox.send_keys('Купить павлиньи перья')

        # Когда она нажимает enter, страница обновляется, и теперь
        # страница содержит "1: Купить павлиньи перья" в качестве
        # элемента списка
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.driver.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        assert any(row.text == "1: Купить павлиньи перья" for row in rows)

        # Текстовое поле по-прежнему приглашает ее добавить еще один
        # элемент. Она вводит "Сделать мушку из павлиньих перьев"
        assert False, "Дописать тест!"

        # Старница обновляется и теперь показывает оба элемента ее
        # списка
