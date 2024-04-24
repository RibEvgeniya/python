
from django.urls import path
from . import views
import os

urlpatterns = [
    path('client/<int:id>/',views.client_detail),
    path('client/list',views.client_list)
]