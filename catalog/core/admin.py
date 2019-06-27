from django.contrib import admin
from core.models import Pants


@admin.register(Pants)
class PantsAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'brand', 'model',
                    'color', 'material',)
    readonly_fields = ["profit"]
