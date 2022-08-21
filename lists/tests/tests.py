import time
from django.test import TestCase

from lists.models import Item


class HomePageTest(TestCase):
    def test_home_page_return_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_save_item_when_necessary(self):
        response = self.client.get('/')
        assert Item.objects.count() == 0

    def test_can_save_a_POST_request(self):
        self.client.post('/', data={'new_item_text': 'A new list item'})
        assert Item.objects.count() == 1
        new_item = Item.objects.first()
        assert 'A new list item' in new_item.text

    def test_redirects_aftre_POST(self):
        response = self.client.post('/', data={'new_item_text': 'A new list item'})
        assert response.status_code == 302
        assert response['Location'] == '/'

    def test_display_all_list_items(self):
        Item.objects.create(text='itemy 1')
        Item.objects.create(text='itemy 2')

        response = self.client.get('/')

        assert 'itemy 1' in response.content.decode()
        assert 'itemy 2' in response.content.decode()


class ItemModelTest(TestCase):
    """Тест модели элемента списка"""

    def test_saving_and_retrieving_items(self):
        """Тест сохранения и получения элементов списка"""
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        assert saved_items.count() == 2

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        assert first_saved_item.text == 'The first (ever) list item'
        assert second_saved_item.text == 'Item the second'

