from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:tea_id>/', views.detail, name='detail'),
    path('<int:tea_id>/timer/', views.timer, name='timer'),
]
