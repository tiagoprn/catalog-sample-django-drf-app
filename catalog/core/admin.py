from django.contrib import admin
from django.contrib.auth.models import User, Group

from config.settings import PAGINATION_ITEMS_PER_PAGE
from core.models import Pants


@admin.register(Pants)
class PantsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    list_per_page = PAGINATION_ITEMS_PER_PAGE
    list_display = ('id', 'brand', 'model', 'color', 'material',
                    'cost_price', 'sell_price', 'profit', 'taxes',
                    'created', 'updated')
    list_filter = ('created', 'updated', )
    search_fields = list_display

# Removes the default apps from the apps menu
admin.site.unregister(User)
admin.site.unregister(Group)

# Change the site header, title and index title
admin.site.site_header = "Pants Catalog"
admin.site.site_title = "Pants Catalog Navigation Site"
admin.site.index_title = ('Click the Pants link below to '
                          'navigate through the database.')
