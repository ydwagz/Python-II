from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Shop.urls')),
    path('Shop/', include('Shop.urls')),
    path('blog/', include("blog.urls")),
]
