"""op_data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from rest_framework.documentation import include_docs_urls
router = DefaultRouter()
from tasks.views import  TaskCreateViewSet, TablefieldsViewSet, SeleFieldFilterViewSet


router = DefaultRouter()
router.register(r'tasks', TaskCreateViewSet, basename='tasks')
router.register(r'tasksSelectTable', TablefieldsViewSet, basename='tasksSelectTable')
router.register(r'SeleFieldFilter', SeleFieldFilterViewSet, basename='SeleFieldFilter')
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^', include(router.urls)),
    url(r'docs/', include_docs_urls(title="归档管理系统")),
]
