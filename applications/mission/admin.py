from django.contrib import admin
from .models import Mission, ExtraFields


class ExtraFieldsAdmin(admin.TabularInline):
    model = ExtraFields
    max_num = 6
    extra = 1


class MissionAdmin(admin.ModelAdmin):
    model = Mission
    inlines = [ExtraFieldsAdmin]
    list_display = ['title', 'sub_title']


admin.site.register(Mission, MissionAdmin)
