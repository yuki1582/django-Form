from django.urls import path
from . import views

app_name = 'form_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('form_page/', views.form_page, name='form_page'),
    path('form_post/', views.form_post, name='form_post'),

]