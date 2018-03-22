from django.conf.urls import url
from . import views

app_name = 'poll'
urlpatterns = [
    url(r'^$',                           views.list,   name='poll_list'),
    url(r'^(?P<pk>\d+)/$',               views.detail, name='poll_detail'),
    url(r'^(?P<pk>\d+)/result/$',        views.result, name='poll_result'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote,   name='poll_vote'),
]