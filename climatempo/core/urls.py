from django.urls import path

from . import views

urlpatterns = [
    path('', views.ClimaTempoView.as_view()),

]
