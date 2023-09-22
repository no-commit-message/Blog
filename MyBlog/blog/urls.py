from django.urls import path
from blog.views import Index, Detail

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('detail/<int:pk>/', Detail.as_view(), name='detail'),
]
