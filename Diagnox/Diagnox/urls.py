"""
URL configuration for Diagnox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from accounts import views as v2
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.acc,name="index"),
    path('signin',v2.signin,name="signin"),
    path('signup',v2.signup,name="signup"),
    path('logout/', views.logout_v, name='logout'),
    path('profile',v2.profile,name="profile"),
    path('password_change',v2.password_change,name="password_change"),
    path('profile/picture/upload/', views.profile_picture_upload, name='profile_picture_upload'),
    path('form',views.formulaire),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
