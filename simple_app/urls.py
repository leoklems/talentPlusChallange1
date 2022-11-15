from django.contrib import admin
from django.urls import path, include
from. import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.display_view),
]

urlpatterns = format_suffix_patterns(urlpatterns)