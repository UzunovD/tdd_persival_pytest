from django.shortcuts import redirect, render
from django.urls import reverse

from lists.models import Item


def home_page(request):
    """Домашняя страница"""
    if request.method == 'POST':
        Item.objects.create(text=request.POST['new_item_text'])
        return redirect(reverse('home'))
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
