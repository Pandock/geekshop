from django.conf.urls import url
from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
   url('^$', mainapp.products, name='index'),
   # url(r'^category/(?P<pk>\d+)/$', mainapp.products, name='product'),
   path('category/<int:pk>/', mainapp.products, name='category'),
]
