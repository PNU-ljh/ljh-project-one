from django.urls import path
from . import views

app_name = 'mypage'

urlpatterns = [
    path('', views.content_list),
    path('<int:pk>/', views.content_detail),
]