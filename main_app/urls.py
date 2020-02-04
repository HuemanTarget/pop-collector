from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pops/', views.pops_index, name='index'),
    path('pops/<int:pop_id>/', views.pops_detail, name='detail'),
]