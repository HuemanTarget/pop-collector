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
    path('pops/<int:pop_id>/add_photo/', views.add_photo, name='add_photo'),
    path('pops/<int:pop_id>/assoc_accessory/<int:accessory_id>/', views.assoc_accessory, name='assoc_accessory'),
    path('accessory/', views.AccessoryList.as_view(), name='accessorys_index'),
    path('accessory/<int:pk>/', views.AccessoryDetail.as_view(), name='accessory_detail'),
    path('accessory/create/', views.AccessoryCreate.as_view(), name='accessory_create'),
    path('accessory/<int:pk>/update/', views.AccessoryUpdate.as_view(), name='accessory_update'),
    path('accessory/<int:pk>/delete/', views.AccessoryDelete.as_view(), name='accessory_delete'),
]