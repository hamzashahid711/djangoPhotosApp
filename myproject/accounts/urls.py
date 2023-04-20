from django.contrib import admin
from django.urls import path
from accounts.views import login_view
from . import views
from .views import register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),


]
