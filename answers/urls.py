"""smartdj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.views.generic.base import RedirectView

from answers.views import predict,intro,judge,regist,login,file_download,file_upload,file_list
from django.conf import settings
urlpatterns = [
    url(r'^$', predict,name='answers'),
    url(r'^intro/$', intro ,name='intro'),
    url(r'^judge/$', judge ,name='judge'),
    url(r'^regist/', regist,name='regist'),
    url(r'^login/', login,name='login'),
    url(r'^download/$', file_list,name='download'),
    url(r'^download/(?P<file>[^/]+)/', file_download,name='download'),
    url(r'^upload/', file_upload,name='upload'),
    url(r'^favicon.ico$', RedirectView.as_view(url=r'static/favicon.ico')),

    # url(r'^intro/', predict),
]
