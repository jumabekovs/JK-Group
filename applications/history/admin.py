from django.contrib import admin
from .models import History, ExtraFields


class ExtraFieldsAdmin(admin.TabularInline):
    model = ExtraFields
    max_num = 6
    extra = 1


class HistoryAdmin(admin.ModelAdmin):
    model = History
    inlines = [ExtraFieldsAdmin]
    list_display = ['title', 'sub_title']


admin.site.register(History, HistoryAdmin)
