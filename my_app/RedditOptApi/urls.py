from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.outputlist.as_view())

]
