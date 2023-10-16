from django.db import models
from django.contrib.auth.models import User

class Main(models.Model):
    title = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(max_length=25000, verbose_name='Содержание')

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'
        ordering = ['title']

    def __str__(self):
        return self.title

class Category(models.Model):
    username = User.objects.values_list('username', 'username')
    title = models.CharField(max_length=100, verbose_name='Наименование')
    created = models.DateTimeField(auto_now_add=True)
    authors = models.CharField(max_length=250, verbose_name='Автор', choices=username)

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['created']

    def __str__(self):
        return self.title


class Note(models.Model):
    username = User.objects.values_list('username', 'username')
    title = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(max_length=25000, verbose_name='Содержание')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notes', verbose_name='Категория')
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False, blank=True, verbose_name='Статус')
    authors = models.CharField(max_length=250, verbose_name='Автор', choices=username)

    class Meta:
        verbose_name_plural = 'Заметки'
        verbose_name = 'Заметки'
        ordering = ['-created']

    def __str__(self):
        return self.title