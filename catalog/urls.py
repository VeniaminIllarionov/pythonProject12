from django.urls import path

from catalog.apps import NewappConfig
from catalog.views import home, contacts, products, product_detail

app_name = NewappConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contacts, name='contact'),
    path('product/', products, name='product'),
    path('product/<int:pk>/', product_detail, name='product_detail')
]