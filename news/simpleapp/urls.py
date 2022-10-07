from django.urls import path
# Импортируем созданные нами представления
from .views import NewsList, NewsDetail, NewsSearch

urlpatterns = [
   path('news/', NewsList.as_view()),
   path('news/<int:pk>', NewsDetail.as_view()),
   path('search/', NewsSearch.as_view())
]
