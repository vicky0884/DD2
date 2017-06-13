"""DD URL Configuration

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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from SU import views as su_views
from anyuser import views as anyuser_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', auth_views.login),

    url(r'^list/', login_required(su_views.viewlist)),#need to check if its working for non logged in users
    url(r'^view*', login_required(su_views.view_doc)),
    url(r'^approve*', login_required(su_views.approve_doc)),
    url(r'^reject*', login_required(su_views.reject_doc)),

    url(r'^upload/', anyuser_views.upload_page),
    url(r'^upload.do', anyuser_views.upload),
]
