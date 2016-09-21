from django.conf.urls import url

from . import views

app_name = 'todo'
urlpatterns = [
    url(r'^$', views.tasklist, name='index'),
    url(r'create/', views.createtask, name='create'),
    url(r'showform/', views.showform),
]
