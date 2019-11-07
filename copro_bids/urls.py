from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/<int:pk>', views.project_detail, name='project_detail'),
    path('project/new', views.project_create, name='project_create'),
    path('project/<int:pk>/edit', views.project_edit, name='project_edit'),

    path('teammate/new', views.teammate_create, name='teammate_create'),
    path('teammate/list', views.teammate_list, name='teammate_list'),
    path('teammate/<int:pk>', views.teammate_detail, name='teammate_detail'),
    path('teammate/<int:pk>/edit', views.teammate_edit, name='teammate_edit'),
    path('teammate/<int:pk>/delete', views.teammate_delete, name='teammate_delete'),

    path('bid/new/', views.bid_create, name='bid_create'),
    path('bid/<int:pk>', views.bid_detail, name='bid_detail'),
    path('bid/<int:pk>/edit', views.bid_edit, name='bid_edit'),
    path('bid/<int:pk>/delete', views.bid_delete, name='bid_delete'),
]
