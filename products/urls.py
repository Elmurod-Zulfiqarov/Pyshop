from django.urls import path
from .views import index, new

urlpatterns = [
    path('', index, name='products'),
    path('new', new, name='new_products'),
]
