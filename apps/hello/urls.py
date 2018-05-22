from django.conf.urls import url, patterns
from apps.hello import views

urlpatterns = patterns(
    'apps.hello.views',
    url(r'^$', views.index,
        name='home'),
)
