from django.contrib import admin
from .models import Line, ExtraFields


class ExtraFieldsAdmin(admin.TabularInline):
    model = ExtraFields
    max_num = 6
    extra = 1


class LineAdmin(admin.ModelAdmin):
    model = Line
    inlines = [ExtraFieldsAdmin]
    list_display = ['company', 'title']


admin.site.register(Line, LineAdmin)
