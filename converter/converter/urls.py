from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('users/', include('users.urls')),
    path("accounts/", include("django.contrib.auth.urls")),

]
