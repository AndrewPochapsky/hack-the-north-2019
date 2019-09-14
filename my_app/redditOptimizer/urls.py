# todos/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('viewInput/', views.ListInput.as_view()),
    path('<pk>/viewInput/', views.ListInput.as_view()),
    path('createInput/', views.ListCreateInput.as_view()),
    path('<pk>/deleteInput/', views.ListDeleteInput.as_view()),

    path('viewOutput/', views.ListOutput.as_view()),
    path('<pk>/viewOutput/', views.ListOutput.as_view()),
    path('createOutput/', views.ListCreateOutput.as_view()),
    path('<pk>/deleteOutput/', views.ListDeleteOutput.as_view())

]
