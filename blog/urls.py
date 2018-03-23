from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.blog_list, name='blog_list'),
    url(r'^(?P<pk>\d+)/$', views.blog_detail, name='blog_detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.blog_edit, name='blog_edit'),
    url(r'^new/$', views.blog_new, name='blog_new'),
    url(r'^(?P<pk>\d+)/delete/$', views.blog_delete, name='blog_delete'),
    url(r'^category/$', views.blog_category_count, name='blog_category_count'),

    url(r'^(?P<pk>\d+)/comment/$', views.comment_list, name='blog_comment_list'),
    url(r'^(?P<pk>\d+)/comment/new/$', views.comment_new, name='blog_comment_new'),
    url(r'^(?P<pk>\d+)/comment/(?P<id>\d+)/delete/$', views.comment_delete, name='blog_comment_delete'),
]

