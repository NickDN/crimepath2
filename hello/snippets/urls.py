from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
import hello.views as  views

urlpatterns = [
    url(r'^path/$', views.snippet_list),
    url(r'^path/(?P<pk>[0-9]+)$', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
