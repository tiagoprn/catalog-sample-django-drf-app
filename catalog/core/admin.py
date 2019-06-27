from django.contrib import admin
from core.models import Pants


@admin.register(Pants)
class PantsAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'brand', 'model', 'color', 'material',
                    'cost_price', 'sell_price', 'profit', 'taxes',
                    'created', 'updated')
    list_filter = ('created', 'updated', )
    search_fields = list_display


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.list_display_links = (None, )


# class LogEntryAdmin(ModelAdmin):
#     actions = None
#     list_display = (
#         'action_time', 'user',
#         'content_type', 'object_repr',
#         'change_message')
#
#     search_fields = ['=user__username', ]
#     fieldsets = [
#         (None, {'fields':()}),
#         ]
#
#     def __init__(self, *args, **kwargs):
#         super(LogEntryAdmin, self).__init__(*args, **kwargs)
#         self.list_display_links = (None, )
