from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.tasklist, name='index'),
    url(r'create/', views.createtask, name='create-task'),
]
