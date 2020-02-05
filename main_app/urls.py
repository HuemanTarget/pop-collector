from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pops/', views.pops_index, name='index'),
    path('pops/<int:pop_id>/', views.pops_detail, name='detail'),
    path('pops/create/', views.PopCreate.as_view(), name='pops_create'),
    path('pops/<int:pk>/update/', views.PopUpdate.as_view(), name='pops_update'),
    path('pops/<int:pk>/delete/', views.PopDelete.as_view(), name='pops_delete'),
    path('pops/<int:pop_id>/add_detail/', views.add_detail, name='add_detail'),
]