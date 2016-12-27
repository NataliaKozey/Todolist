from django.conf.urls import include, url
from . import views


urlpatterns =[
    url(r'^todolist/get/(?P<TO_DO_LIST_id>\d+)/$', views.todo, name='todo'),
    url(r'^$', views.todolist, name='todolist'),
    url(r'^todolist/add_category/$', views.new_category, name='add_category'),
    url(r'^todolist/addnew/$', views.addnew, name='addnew'),
    url(r'^todolist/addnew/savetodolist/$', views.savetodolist),
    url(r'^page/(\d+)/todolist/done/(?P<TO_DO_LIST_id>\d+)/$', views.done, name='done'),
    url(r'^todolist/done/(?P<TO_DO_LIST_id>\d+)/$', views.done, name='done'),
    url(r'^page/(\d+)/todolist/delete_confirm/(?P<TO_DO_LIST_id>\d+)/$', views.delete_confirm, name='delete_confirm'),
    #url(r'^page/(\d+)/todolist/delete_confirm/(?P<TO_DO_LIST_id>\d+)/delete/$', 'task_list.views.delete'),
    url(r'^todolist/delete_confirm/(?P<TO_DO_LIST_id>\d+)/$', views.delete_confirm, name='delete_confirm'),
    #url(r'^todolist/delete_confirm/(?P<TO_DO_LIST_id>\d+)/delete/$', 'task_list.views.delete'),
    url(r'^page/(\d+)/$', views.todolist, name='todolist'),

    url(r'^todolist/add_category/save_category/$', views.save_category, name='save_category'),

]