from django.core.mail import send_mail
from rest_framework import serializers

from source import settings
from .models import Vacancy, CV


class VacancyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = "__all__"


class VacancyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = "__all__"


class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = "__all__"

    def get_cv_url(self, obj):
        if obj.cv:
            url = obj.cv.url
            requests = self.context.get("request")
            if requests is not None:
                url = requests.build_absolute_uri(url)
        else:
            url = ""
        return url

    def create(self, validated_data):
        message = CV.objects.create(**validated_data)
        vacancy = validated_data.get('vacancy')
        cv = validated_data.get('cv')
        send_mail('Новое сообщение',
                  message=f'Отправили резюме:\t https://res.cloudinary.com/dn17ltczr/image/upload/v1/{message}\t '
                          f'на вакансию\t{vacancy}',
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=["baiyshbeksultanov1@gmail.com"],
                  fail_silently=False)
        print(message)
        return message
