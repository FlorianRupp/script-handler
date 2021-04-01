from handler import views

from django.urls import path


urlpatterns = [
    path("", views.execute)
]