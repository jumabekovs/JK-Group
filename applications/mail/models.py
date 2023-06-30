from django.core.validators import RegexValidator
from django.db import models


class Mail(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=256)
    email = models.EmailField(verbose_name='Эл.почта', max_length=256)
    phone_regex = RegexValidator(regex=r'^\+?996?\d{9}$',
                                 message="номер должен начинаться на +996 и еще 9 цифр")
    phone_number = models.CharField(validators=[phone_regex], max_length=13)
    question = models.TextField(verbose_name='вопрос')

    def __str__(self):
        return f"{self.name} - {self.email} - {self.phone_number}"

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
