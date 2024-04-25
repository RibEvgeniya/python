
from django.urls import path
from . import views
import os

urlpatterns = [
    path('client/<int:id>/',views.client_detail),
    path('client/list',views.client_list),
    path('',views.client_list),
    path('client/add',views.client_create),
    path('client/<int:id1>/update',views.client_update)
]