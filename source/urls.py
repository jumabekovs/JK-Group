"""
URL configuration for source project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="JK Group Web API",
        default_version='v1',
        description="JK Group Web Development",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('summernote/', include('django_summernote.urls')),
]

urlpatterns += i18n_patterns(
    path('career/', include('applications.career.urls')),
    path('company/', include('applications.company.urls')),
    path('line/', include('applications.line.urls')),
    path('history/', include('applications.history.urls')),
    path('main/', include('applications.main.urls')),
    path('posts/', include('applications.news.urls')),
    path('partners/', include('applications.partner.urls')),
    path('projects/', include('applications.project.urls')),
    path('team/', include('applications.staff.urls')),
    path('vacancies/', include('applications.vacancy.urls')),
    # path('contacts/', include('applications.mail.urls')),
)


admin.site.site_header = 'JK Group'
admin.site.index_title = 'Администрирование'
admin.site.site_title = 'JK Group Admin'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)