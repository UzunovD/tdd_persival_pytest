from django.shortcuts import render


def home_page(request):
    """Домашняя страница"""
    if request.method == 'POST':
        to_do_item = request.POST['item_text']
        context = {'to_do_item': to_do_item}
        return render(request, 'home.html', context=context)
    else:
        return render(request, 'home.html')
