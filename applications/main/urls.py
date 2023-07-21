from django.urls import path
from .views import MainListView

urlpatterns = [
    path("", MainListView.as_view()),
]
"""
        model1_results = Main.objects.filter(title_ru__icontains=query, title_ky__icontains=query)
        model2_results = Project.objects.filter(Q(title_ru__icontains=query) |
                                                Q(title_ky__icontains=query) | Q(title_en__icontains=query))
        model3_results = Partner.objects.filter(Q(title_ru__icontains=query) |
                                                Q(title_ky__icontains=query) | Q(title_en__icontains=query))
        model4_results = Post.objects.filter(Q(title_ru__icontains=query) |
                                             Q(title_ky__icontains=query) | Q(title_en__icontains=query))
        model5_results = Line.objects.filter(Q(title_ru__icontains=query) |
                                             Q(title_ky__icontains=query) | Q(title_en__icontains=query))
"""