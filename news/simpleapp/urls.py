from django.urls import path
# Импортируем созданные нами представления
from .views import ProductsList, ProductDetail, NewsList, NewsDetail

urlpatterns = [
   path('products/', ProductsList.as_view()),
   path('products/<int:pk>', ProductDetail.as_view()),
   path('news/', NewsList.as_view()),
   path('news/<int:pk>', NewsDetail.as_view())
]
