"""VGG URL Configuration

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
from .views import *
from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet
from .api import router



#router.register(r'accounts', AccountViewSet)



urlpatterns = [
    #url(r'^', include(router.urls)),
	path("index/",index, name="home"),
	path('api/v1/', include(router.urls)),

]


    # 6 GET REQUESTS
    # path("api/project",index, name="home")
    # path("api/projects/<projectid>",index, name="home")
    # path("api/project/<projectid>",index, name="home")
    # path("api/actions",index, name="home")
    # path("api/actions/<actionid>",index, name="home")
    # path("api/projects/<projectId>/actions/<actionId>",index, name="home")

    # 4 POST REQUESTS
    # path("api/users/register",index, name="home")
    # path("api/projects",index, name="home")
    # path("api/users/auth",index, name="home")
    # path("api/projects/<projectId>/actions",index, name="home")

    # 2 DELETE REQUESTS
    # path("api/projects/<projectId>",index, name="home")
    # path("api/projects/<projectId>/actions/<actionId>",index, name="home")

	# 2 PUT REQUESTS
    # path("api/projects/<projectId>",index, name="home")
    # path("api/projects/<projectId>/ actions/<actionId>",index, name="home")

	# 1 PATCH REQUESTS
    # path("api/projects/<projectId>",index, name="home")

   
