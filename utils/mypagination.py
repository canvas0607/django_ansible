from rest_framework.pagination import LimitOffsetPagination

class CustomPagination(LimitOffsetPagination):
    max_limit = 1000
    default_limit = 1000