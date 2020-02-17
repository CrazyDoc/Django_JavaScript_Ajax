from django.contrib import admin
from django.urls import include, path, re_path
from firstapp import views
 
urlpatterns = [
    path('', views.index),
    path('dataurl', views.AjaxData),
    path('dateurl/<str:table_name>', views.DateData)
]