from django.conf.urls import include, url
from task_list.views import *


urlpatterns = [

    url(r'^todolist/get/(?P<TO_DO_LIST_id>\d+)/$', todo),
    url(r'^$', 'task_list.views.todolist'),
    url(r'^todolist/add_category/$', new_category),
    url(r'^todolist/addnew/$', addnew),
    url(r'^todolist/addnew/savetodolist/$', savetodolist),
    url(r'^page/(\d+)/todolist/done/(?P<TO_DO_LIST_id>\d+)/$', done),
    url(r'^todolist/done/(?P<TO_DO_LIST_id>\d+)/$', done),
    url(r'^page/(\d+)/todolist/delete_confirm/(?P<TO_DO_LIST_id>\d+)/$', delete_confirm),
    #url(r'^page/(\d+)/todolist/delete_confirm/(?P<TO_DO_LIST_id>\d+)/delete/$', 'task_list.views.delete'),
    url(r'^todolist/delete_confirm/(?P<TO_DO_LIST_id>\d+)/$', delete_confirm),
    #url(r'^todolist/delete_confirm/(?P<TO_DO_LIST_id>\d+)/delete/$', 'task_list.views.delete'),
    url(r'^page/(\d+)/$', todolist),

    url(r'^todolist/add_category/save_category/$', save_category),

    # url(r'^todolist/get/(?P<TO_DO_LIST_id>\d+)/$', 'task_list.views.todo'),
    # url(r'^$', 'task_list.views.todolist'),
    # url(r'^todolist/add_category/$', 'task_list.views.new_category'),
    # url(r'^todolist/addnew/$', 'task_list.views.addnew'),
    # url(r'^todolist/addnew/savetodolist/$', 'task_list.views.savetodolist'),
    # url(r'^page/(\d+)/todolist/done/(?P<TO_DO_LIST_id>\d+)/$', 'task_list.views.done'),
    # url(r'^todolist/done/(?P<TO_DO_LIST_id>\d+)/$', 'task_list.views.done'),
    # url(r'^page/(\d+)/todolist/delete_confirm/(?P<TO_DO_LIST_id>\d+)/$', 'task_list.views.delete_confirm'),
    # #url(r'^page/(\d+)/todolist/delete_confirm/(?P<TO_DO_LIST_id>\d+)/delete/$', 'task_list.views.delete'),
    # url(r'^todolist/delete_confirm/(?P<TO_DO_LIST_id>\d+)/$', 'task_list.views.delete_confirm'),
    # #url(r'^todolist/delete_confirm/(?P<TO_DO_LIST_id>\d+)/delete/$', 'task_list.views.delete'),
    # url(r'^page/(\d+)/$', 'task_list.views.todolist'),

    # url(r'^todolist/add_category/save_category/$', 'task_list.views.save_category'),

]