from django.urls import path

from catalog.apps import NewappConfig
from catalog.views import contacts, ProductDetailView, ProductListView

app_name = NewappConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contact/', contacts, name='contact'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail')
]