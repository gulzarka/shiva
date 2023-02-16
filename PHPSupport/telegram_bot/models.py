from datetime import datetime

from django.db import models


class Clarification(models.Model):
    question = models.TextField('question')
    answer = models.TextField('answer')
    creation_date = models.DateTimeField('request creation date', auto_now=True, auto_now_add=True)


class Request(models.Model):
    creation_date = models.DateTimeField('request creation date', auto_now=True, auto_now_add=True)
    title = models.CharField('title', max_length=50)
    description = models.TextField('description')
    price = models.IntegerField('price', blank=True, null=True)
    estimate = models.DateTimeField('estimate', blank=True, null=True)
    php_login = models.CharField('php login', max_length=50)
    php_password = models.CharField('php password', max_length=50)
    php_link = models.CharField('php link', max_length=50)
    clarification = models.ForeignKey(Clarification, verbose_name='clarification', on_delete=models.CASCADE)

    class RequestStatus(models.TextChoices):
        PENDING = 'PNDG', ('pending')
        OPEN = 'OPEN', ('open')
        WORKING = 'WORK', ('in working')
        COMPLETE = 'CMPL', ('complete')
        CANCELLED = 'CNLD', ('cancelled')

    status = models.CharField(
        max_length=4,
        choices=RequestStatus.choices,
        default=RequestStatus.PENDING,
    )

    class RequestDifficulty(models.TextChoices):
        EASY = 'EASY', ('easy')
        MEDIUM = 'MEDM', ('medium')
        HARD = 'HARD', ('hard')

    difficulty = models.CharField(
        max_length=4,
        choices=RequestDifficulty.choices,
    )


class Client(models.Model):
    name = models.CharField('name', max_length=50)
    telegram_id = models.CharField('telegram id', max_length=50)
    registration_date = models.DateTimeField('date of registration', auto_now=True, auto_now_add=True)
    subscription_end = models.DateTimeField('end of subscription date')
    request = models.ForeignKey(Request, on_delete=models.CASCADE, verbose_name='client request', null=True, blank=True)

    @property
    def is_active(self):
        if datetime.now() < self.subscription_end:
            return True
        else:
            return False


class Subcontractor(models.Model):
    name = models.CharField('name', max_length=50)
    telegram_id = models.CharField('telegram id', max_length=50)
    registration_date = models.DateTimeField('date of registration', auto_now=True, auto_now_add=True)
    salary = models.IntegerField('salary', blank=True, null=True)
    is_active = models.BooleanField('is active', blank=True, null=True)
    request = models.ForeignKey(Request, on_delete=models.SET_NULL, verbose_name='subcontractor request', null=True, blank=True)
