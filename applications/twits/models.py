from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    """
    Вопрос
    """

    # Текст вопроса
    text = models.CharField(max_length=250, blank=True, null=False, default='')

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.text


class Customer(models.Model):

    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)


class Good(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    price = models.FloatField(null=False, default=0.0)


class Order(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    goods = models.ManyToManyField(to=Good)


class Person(models.Model):
    """Добавление подписки"""

    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')


class Post(models.Model):
    """Сообщения"""

    text = models.CharField(max_length=1000, blank=True, null=False, default='')
    author = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'


class Comment(models.Model):
    """Коментарии"""

    text = models.CharField(max_length=1000, blank=True, null=False, default='')
    parent = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
