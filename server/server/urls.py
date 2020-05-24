"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from posts.views import PostViewSet, PostSWViewSet
from user.views import UserViewSet, LostFindViewSet

# Router
router = routers.DefaultRouter()
router.register('posts', PostViewSet) # prefix = posts , viewset = PostViewSet
router.register('posts_sw', PostSWViewSet) # prefix = posts_sw, viewset = PostSWViewSet
router.register('user', UserViewSet)
router.register('lost-find', LostFindViewSet)

# URL Patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    path('auth/', obtain_auth_token, name='auth'),
]
