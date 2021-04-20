"""champaksite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.urls import path
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)

urlpatterns = [

 path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	
    path('admin/', admin.site.urls),
path("getbook/",views.getbook),
path("allbooks/",views.allbooks),
path("addbook/",views.addbook),
	path("mybook/",views.mybook),
	path("multiply/",views.multiply),
	path("'calculator/",views.calculator),
path("simpleurl/", views.simpleurl),
path("templateview/", views.templateview),
path("testview/", views.testview),
path("sub/", views.suburl),
path("setsession/",views.setsession),
path("getsession/",views.getsession),
path("dologin/",views.dologin),
path("protected/",views.protected),
path("logincheck/",views.logincheck),
path("showdata/",views.showdata),
path("", views.index),
]
