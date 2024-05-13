from django.urls import path

from catalog.apps import NewappConfig
from catalog.views import home, contacts, products

app_name = NewappConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contacts, name='contact'),
    path('product/', products, name='product'),
]