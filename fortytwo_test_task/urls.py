from django.conf.urls import patterns, include, url

from django.contrib import admin
from apps.hello import urls as hello_urls

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include(hello_urls, namespace='hello')),
    url(r'^admin/', include(admin.site.urls)),
)
