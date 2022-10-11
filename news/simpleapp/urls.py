from django.urls import path
# Импортируем созданные нами представления
from .views import NewsList, NewsDetail, NewsSearch, NewsCreate

urlpatterns = [
   # path('news/', NewsList.as_view()),
   path('<int:pk>', NewsDetail.as_view()),
   path('search/', NewsSearch.as_view()),
   path('', NewsList.as_view(), name='news_list'),
   path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
   path('create/', NewsCreate.as_view(), name='news_create'),
]
