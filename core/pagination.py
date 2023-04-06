from rest_framework.pagination import LimitOffsetPagination

from core import settings


class OffsetPagination(LimitOffsetPagination):
    page_size = settings.REST_FRAMEWORK["PAGE_SIZE"]
    max_limit = settings.REST_FRAMEWORK["MAX_LIMIT"]
