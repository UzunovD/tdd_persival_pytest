import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def setup(request):
    driver = webdriver.Firefox()
    request.instance.driver = driver
    driver.get('http://localhost:8000')
    yield driver
    driver.close()


@pytest.mark.usefixtures('setup')
class Test:
    def check_for_row_in_list_table(self, row_text:str):
        table = self.driver.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        assert row_text in [row.text for row in rows]

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
        # wait = WebDriverWait(self.driver, 10)
        time.sleep(1)

        self.check_for_row_in_list_table("1: Купить павлиньи перья")
        # Текстовое поле по-прежнему приглашает ее добавить еще один
        # элемент. Она вводит "Сделать мушку из павлиньих перьев"
        inputbox = self.driver.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Сделать мушку из павлиньих перьев')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        # Старница обновляется и теперь показывает оба элемента ее
        # списка
        self.check_for_row_in_list_table("1: Купить павлиньи перья")
        self.check_for_row_in_list_table("2: Сделать мушку из павлиньих перьев")

        assert False, "Дописать тест!"

