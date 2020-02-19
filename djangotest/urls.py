from django.contrib import admin
from django.urls import include, path, re_path
from firstapp import views
 
urlpatterns = [
    path('', views.index),
    path('dataurl', views.AjaxData),
    path('dateurl/ps<str:dateinterval>', views.DateData)
]