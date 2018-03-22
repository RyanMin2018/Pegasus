"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^\Z',     include('main.urls')),
    url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^account/join/$', views.CreateUserView.as_view(), name='join'),
    url(r'^account/join/complete/$', views.RegisteredView.as_view(), name='join_complete'),
    url(r'^blog/',  include('blog.urls')),
    url(r'^poll/',  include('poll.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
