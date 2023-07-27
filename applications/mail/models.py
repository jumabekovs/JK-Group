from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from applications.line.models import Line


class Mail(models.Model):
    line = models.ForeignKey(Line, verbose_name='направление', related_name='mail_line', on_delete=models.DO_NOTHING, null=True)
    name = models.CharField(verbose_name=_('Имя'), max_length=256)
    email = models.EmailField(verbose_name=_('Эл.почта'), max_length=256)
    phone_regex = RegexValidator(regex=r'^\+?996?\d{9}$',
                                 message=_("номер должен начинаться на +996 и еще 9 цифр"))
    phone_number = models.CharField(validators=[phone_regex], max_length=13, verbose_name=_("номер телефона"))
    question = models.TextField(verbose_name=_('ваш вопрос'))

    def __str__(self):
        return f"{self.name} - {self.email} - {self.phone_number}"

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
