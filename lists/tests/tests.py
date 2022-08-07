from django.test import TestCase
from django.http import HttpRequest
from lists import views


class Test:
    def test_home_page_return_correct_html(self):
        """Проверяет корректность ответа home_page"""
        request = HttpRequest()
        html = views.home_page(request).content.decode('utf-8')
        assert '<html><title>To-Do lists</title></html>' in html
