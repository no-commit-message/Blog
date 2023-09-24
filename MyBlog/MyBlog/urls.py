from django.contrib import admin
from django.urls import path, include
from blog.views import top
from accounts.views import accounts


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', top , name='top'),
    path('accounts/', accounts, name='accounts'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('blog/', include('blog.urls')),
]
