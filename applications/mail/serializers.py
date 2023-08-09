from django.core.mail import send_mail
from rest_framework import serializers

from applications.mail.models import Mail, Tab
from source import settings


class TabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tab
        fields = "__all__"


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = "__all__"

    def create(self, validated_data):
        message = Mail.objects.create(**validated_data)
        email = validated_data.get('email')
        line = validated_data.get('line')
        name = validated_data.get('name')
        phone = validated_data.get('phone_number')
        question = validated_data.get('question')
        send_mail('Новое сообщение',
                  message=f'{line}\nПользователь: {email}\nОставил сообщение:\t {question}\nИмя:\t{name}\nНомер '
                          f'телефона:\t{phone}',
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=["support@jkgroup.kg"],
                  fail_silently=False)
        return message
