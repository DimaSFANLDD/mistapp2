from django.urls import re_path
from .views import sorev_list, sorev_list_published, sorev_detail

urlpatterns = [
    re_path(r'^', sorev_list),
    re_path(r'^sorev/(?P<pk>[0-9]+)$', sorev_detail),
    re_path(r'^sorev/published$', sorev_list_published),
    ]
