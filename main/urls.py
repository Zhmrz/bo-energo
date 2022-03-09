from django.urls import path
from .views import index, page1, page2

urlpatterns = [
    path('', index, name='index'),
    path('page1', page1, name='page1'),
    path('page2', page2, name='page2'),
]