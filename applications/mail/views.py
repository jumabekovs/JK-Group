from rest_framework.generics import CreateAPIView
from .models import Mail
from .serializers import MailSerializer


class CreateMailView(CreateAPIView):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer
