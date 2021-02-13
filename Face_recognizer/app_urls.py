from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [path('',views.home),
               path('recognizer',views.web_feed,name='recognizer'),
               path('web_feed',views.web_feed,name='web_feed'),
               
               path('Attendence', views.Attendence,name='Attendence'),
               path('export/', views.ExportCSV,name='ExportCSV'),
               path('daywise/', views.daywise,name='daywise'),
               
               #path('save',views.save),]
               path('admin/', admin.site.urls,name='admin'),]

               
