"""hhli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

from locations import urls as locations_urls
from users import urls as users_urls
from hhli import settings
from users import views as user_views

from rest_framework import routers
router = routers.DefaultRouter()

# from users import apis as users_apis
# router.register(r'users', users_apis.CustomerViewSet)

from users import viewsets as users_viewsets
router.register(r'users', users_viewsets.HUserViewSet)
router.register(r'edit_users', users_viewsets.HUserEditViewSet)



urlpatterns = [
    url(r'^$', user_views.index, name='index'),
    url(r'^users/', include(users_urls)),
	url(r'^locations/', include(locations_urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_docs.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
