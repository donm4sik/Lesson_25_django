from django.urls import path

from apps.news.views import (
    greeting,
)

urlpatterns = [
    path('', greeting)
]

