from django.core.mail import send_mail
from rest_framework import serializers

from applications.mail.models import Mail
from source import settings


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = "__all__"

    def create(self, validated_data):
        message = Mail.objects.create(**validated_data)
        email = validated_data.get('email')
        name = validated_data.get('name')
        phone = validated_data.get('phone_number')
        question = validated_data.get('question')
        send_mail('Новое сообщение',
                  message=f'Пользователь: {email}\nОставил сообщение:\t {question}\nИмя:\t{name}\nНомер '
                          f'телефона:\t{phone}',
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=["so.fly.azash@gmail.com"],
                  fail_silently=False)
        return message
