from django.conf.urls import patterns, include, url

from tasks import views

urlpatterns = patterns('', 
        url(r'^$', views.index, name='index'),
        url(r'^(?P<task_id>\d+)/$', views.itemlist, name='itemlist'),
        url(r'^(?P<task_id>\d+)/add/$', views.add, name='add'),
        url(r'^(?P<task_id>\d+)/additem/$', views.additem, name='additem'),
        url(r'^addlist$', views.addlist, name='addlist'),
        url(r'^new/$', views.new, name='new'),
        url(r'^login/$', views.login_req, name='login'),
        url(r'^login_user/$', views.login_user, name='login_user'),
        url(r'welcome/$', views.welcome, name='welcome'),
        url(r'signup/$', views.signup, name='signup'),
        url(r'create_user/$', views.create_user, name='create_user'),
        url(r'logout/$', views.logout_user, name='logout_user'),
        url(r'(?P<task_id>\d+)/edititem/(?P<item_id>\d+)/$', views.edit_item,\
            name='edit_item'),
        )
