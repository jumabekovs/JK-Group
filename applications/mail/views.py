from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Mail, Tab
from .serializers import MailSerializer, TabSerializer


class CreateMailView(CreateAPIView):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer


class TabView(ListAPIView):
    queryset = Tab.objects.all()
    serializer_class = TabSerializer
