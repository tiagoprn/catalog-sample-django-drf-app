from django_filters.rest_framework import (
    FilterSet,
    CharFilter,
    NumberFilter,
    DateTimeFilter,
)


class PantsFilter(FilterSet):
    class Meta:
        fields = [
            'brand',
            'model',
            'color',
            'material',
            'min_cost_price',
            'max_cost_price',
            'min_sell_price',
            'max_sell_price',
            'min_profit',
            'max_profit',
            'min_taxes',
            'max_taxes',
            'min_created_at',
            'max_created_at',
            'min_updated_at',
            'max_updated_at',
        ]

    brand = CharFilter(lookup_expr='icontains')
    model = CharFilter(lookup_expr='icontains')
    color = CharFilter(lookup_expr='icontains')
    material = CharFilter(lookup_expr='icontains')
    min_cost_price = NumberFilter(field_name='cost_price', lookup_expr='gte')
    max_cost_price = NumberFilter(field_name='cost_price', lookup_expr='lte')
    min_sell_price = NumberFilter(field_name='sell_price', lookup_expr='gte')
    max_sell_price = NumberFilter(field_name='sell_price', lookup_expr='lte')
    min_profit = NumberFilter(field_name='profit', lookup_expr='gte')
    max_profit = NumberFilter(field_name='profit', lookup_expr='lte')
    min_taxes = NumberFilter(field_name='taxes', lookup_expr='gte')
    max_taxes = NumberFilter(field_name='taxes', lookup_expr='lte')
    min_created_at = DateTimeFilter(field_name='created_at', lookup_expr='gte')
    max_created_at = DateTimeFilter(field_name='created_at', lookup_expr='lte')
    min_updated_at = DateTimeFilter(field_name='updated_at', lookup_expr='gte')
    max_updated_at = DateTimeFilter(field_name='updated_at', lookup_expr='lte')
