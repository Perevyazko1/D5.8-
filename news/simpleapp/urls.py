from django.urls import path
# Импортируем созданные нами представления
from .views import ProductsList, ProductDetail, NewsList, NewsDetail

urlpatterns = [
   path('news/', NewsList.as_view()),
   path('news/<int:pk>', NewsDetail.as_view())
]
