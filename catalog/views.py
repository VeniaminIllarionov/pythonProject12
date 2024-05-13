from django.shortcuts import render

from catalog.models import Category, Product


def home(request):
    category_list = Category.objects.all()
    context = {
        'object_list': category_list
    }
    return render(request, 'home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'У вас новое сообщение: {name}({phone}): {message}')
    return render(request, 'contacts.html')


def products(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'products.html', context)
