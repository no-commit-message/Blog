from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.Index.as_view(), name='index'),
    path('detail/<int:pk>/', views.Detail.as_view(), name='detail'),
    path('create/', views.Create.as_view(), name='create'),
    path('update/<int:pk>/', views.Update.as_view(), name='update'),
    path('delete/<int:pk>/', views.Delete.as_view(), name='delete'),
]
