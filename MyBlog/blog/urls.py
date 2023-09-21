from django.urls import path
from blog.views import top

urlpatterns = [
    path('', top)
]
