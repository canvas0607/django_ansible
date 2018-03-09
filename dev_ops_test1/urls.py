"""dev_ops_test1 URL Configuration

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
import xadmin
from django.conf.urls import url,include
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from server.views import ServerDetailViewSet

router = DefaultRouter()

router.register(r'^servers/detail',ServerDetailViewSet)

urlpatterns = [
    #url(r'^admin/', admin.site.urls),

    url(r'^admin/', xadmin.site.urls),

    # 用户登录
    url(r'^login/user$', obtain_jwt_token, name='user-login'),


    # 自动生成文档使用的接口配置
    url(r"^docs/", include_docs_urls(title="api_doc")),

    #注册drf路由
    url(r'^', include(router.urls)),
]
