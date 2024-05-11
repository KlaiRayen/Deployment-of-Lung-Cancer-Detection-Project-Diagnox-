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
from rendezvous import views as vr
from forum import views as forum_views

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
    path('chatpal/', views.chatpal, name='chatpal'),
    path('rendezvous',vr.listDoc , name="listdoc"),
    path('rendezvous/form/<int:doctor_id>/',vr.create_rendezvous , name="rndvForm"),
    path('fetch_time_slots', vr.fetch_time_slots, name='fetch_time_slots'),
    path('rendezvous/list', vr.showListDocRdv, name='showListDocRdv'),
    path('fetch_dr_rdvs/', vr.listDocRdv, name='fetch_dr_rdvs'),
    path('forum', forum_views.forum_home, name='forum_home'),
    path('forum/thread/create', forum_views.create_thread, name='create_thread'),
   # path('thread/<int:thread_id>/', forum_views.view_thread, name='view_thread'),
    path('forum/thread/<int:thread_id>/post/create', forum_views.create_post, name='create_post'),
    path('forum/thread/<int:thread_id>/', forum_views.view_thread, name='view_thread'),
    path('forum/thread/<str:cat>/', forum_views.threadPerCat, name='threadpercat'),
    path('typeDetection',views.typedetection , name= 'typedetection')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
