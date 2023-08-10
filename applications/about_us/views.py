from rest_framework.generics import ListAPIView

from .models import AboutUs
from .serializers import AboutUsSerializer


class AboutUsView(ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    pagination_class = None
