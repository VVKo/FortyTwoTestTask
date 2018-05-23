from django.conf.urls import url, patterns
from apps.hello import views

app_name = 'hello'

urlpatterns = patterns(
    '',
    url(r'^$', views.ShowPersonalDataView.as_view(),
        name='index'),
)
