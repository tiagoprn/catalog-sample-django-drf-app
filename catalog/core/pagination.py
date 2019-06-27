from rest_framework.pagination import PageNumberPagination

from config.settings import (
    PAGINATION_ITEMS_PER_PAGE,
    PAGINATION_ITEMS_MAX_PAGE_SIZE,
)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = PAGINATION_ITEMS_PER_PAGE
    page_size_query_param = 'page_size'
    max_page_size = PAGINATION_ITEMS_MAX_PAGE_SIZE
