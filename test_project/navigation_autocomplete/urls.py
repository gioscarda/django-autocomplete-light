from django.urls import re_path
from .views import navigation_autocomplete

urlpatterns = [
    re_path(r'^$', navigation_autocomplete, name='navigation_autocomplete'),
]
