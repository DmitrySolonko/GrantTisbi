from django.db import models


# Create your models here.
from django.urls import reverse


class Articles(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    icon = models.FileField(upload_to='icons/%Y/%m/%d/', verbose_name='Иконка', blank=True)
    description = models.TextField(verbose_name='Краткое описание')
    content = models.TextField(verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_page", kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['created_at']


class FeedBack(models.Model):
    FIO = models.CharField(max_length=100, verbose_name='ФИО')
    email = models.CharField(max_length=150, verbose_name='Почтовый адрес')
    text = models.TextField(verbose_name='Сообщение')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')

    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name = 'заявка из обратной связи'
        verbose_name_plural = 'заявки из обратной связи'
        ordering = ['-date']