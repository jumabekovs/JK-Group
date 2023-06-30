from django.contrib import admin
from .models import Career, CareerImages


class CareerImagesAdmin(admin.TabularInline):
    model = CareerImages
    max_num = 6
    extra = 1


class CareerAdmin(admin.ModelAdmin):
    model = Career
    inlines = [CareerImagesAdmin]
    list_display = ['title']


admin.site.register(Career, CareerAdmin)
