from django.db import models
from django.core.validators import MinValueValidator


# Товар для нашей витрины
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True, # названия товаров не должны повторяться
    )
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
    )
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='products', # все продукты в категории будут доступны через поле products
    )
    price = models.FloatField(
        validators=[MinValueValidator(0.0)],
    )

    # def __iter__(self):
    #     """ возвращаем сам объект """
    #     return f'{self.name.title()}: {self.description[:20]}'


    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'


# Категория, к которой будет привязываться товар
class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=100, unique=True)


    # def __iter__(self):
    #     """ возвращаем сам объект """
    #     return self.name.title()



    def __str__(self):
        return self.name.title()


# Create your models here.
class News(models.Model):
    # NEWS = 'NW'
    # ARTICLE = 'AR'
    # CATEGORY_CHOICES = (
    #     (NEWS, 'Новость'),
    #     (ARTICLE, 'Статья')
    # )
    # categoryType = models.CharField(max_length=2,choices=CATEGORY_CHOICES,
    #                                 default=ARTICLE)
    dateCreation = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        to='NewsCategory',
        on_delete=models.CASCADE,
        related_name='news',  # все продукты в категории будут доступны через поле news
    )
    title = models.CharField(max_length=128)
    text = models.TextField()
    def __str__(self):
        return f'{self.title.title()}: {self.text[:20]}'

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])


class NewsCategory(models.Model):
    name = models.CharField(max_length=100, unique=True,default=None)

    def __str__(self):
        return self.name.title()
