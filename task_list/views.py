from forms import TodolistForm, CategoryForm
from task_list.models import Category, Todolist
from django.shortcuts import render_to_response, redirect
from django.core.paginator import Paginator
from django.template import RequestContext
from django.contrib import auth
from django.views.decorators import csrf
from django.http import Http404, HttpResponseNotFound, HttpResponse
import datetime






def done(request, TO_DO_LIST_id):
    # if request.method == "POST" and "Done" in request.POST:
    #     args = {}
    #     args.update(csrf(request))

    #     args['done']= Todolist.objects.get(id=TO_DO_LIST_id)
    list_todo = Todolist.objects.get(id=TO_DO_LIST_id)
    list_todo.todolist_done = not list_todo.todolist_done

    list_todo.save()
    return redirect('/')
    #return render_to_response('main.html', {"todolist_done": list_todo.todolist_done})

def todolist(request, page_number=1):

    current_user = request.user
    if current_user.is_authenticated():
        todos = Todolist.objects.filter(todolist_user=current_user)
        current_page=Paginator(todos, 4)
        return render_to_response('todolist.html', {'todolist': current_page.page(page_number), 'username': auth.get_user(request).username}, RequestContext(request))
    else:
        return redirect('/auth/login')

"""def todo(request, TO_DO_LIST_id=1):

    return render_to_response('todo.html', {'todo': Todolist.objects.get(id=TO_DO_LIST_id, todolist_user=request.user), 'datetime': DateTime.objects.filter(id = TO_DO_LIST_id),'username': auth.get_user(request).username })"""

def todo(request, TO_DO_LIST_id):
    current_user = request.user
    if current_user.is_authenticated():
        try:
            todo = Todolist.objects.get(id=TO_DO_LIST_id, todolist_user=request.user)
            return render_to_response('todo.html', {'todo': todo, 'username': auth.get_user(request).username })
        except Todolist.DoesNotExist:
            raise Http404("Todolist does not found")


    else:
        return redirect('/auth/login')

# def addnew(request, TO_DO_LIST_id=1):

#     todolist_form = TodolistForm
#     args = {}
#     args.update(csrf(request))
#     args['user'] = request.user
#     #args['datetime']= DateTime.objects.filter(id = TO_DO_LIST_id)
#     #args['mytodo'] = Todolist.objects.get(id=TO_DO_LIST_id)
#     #list = [todolist_form, {'user': request.user}]
#     args['form']= todolist_form
#     return render_to_response('addnew.html', args, RequestContext(request))

# def savetodolist(request):

#     if request.POST:
#         form = TodolistForm(request.POST)
#         if form.is_valid():
#             form.save(request.user, datetime.datetime.now())


#     return redirect('/')
def addnew(request, TO_DO_LIST_id=1):

    todolist_form = TodolistForm
    args = {}
    #args.update(csrf(request))
    args['todolist_user'] = request.user
    args['todolist_date_published'] = datetime.datetime.now()
    
    args['form']= todolist_form
    return render_to_response('addnew.html', args, RequestContext(request))

def savetodolist(request):
    todolist_form = TodolistForm
    args = {}
    #args.update(csrf(request))
    args['todolist_user'] = request.user
    args['todolist_date_published'] = datetime.datetime.now()
    
    args['form']= todolist_form
    if request.POST:
        form = TodolistForm(request.POST)
        if form.is_valid():
            form.save(request.user, datetime.datetime.now())


    return redirect('/')






def new_category(request):
    my_new_category = CategoryForm
    args = {}
    #args.update(csrf(request))
    args['user'] = request.user

    args['forms']= my_new_category
    return render_to_response('category.html', args, RequestContext(request))


def save_category(request):
    if request.POST:
        #forms = CategoryForm(request.POST)
        if CategoryForm(request.POST).is_valid():
            CategoryForm(request.POST).save()

    return redirect('/')

def delete_confirm(request, TO_DO_LIST_id):

    del_todolist = Todolist.objects.get(id=TO_DO_LIST_id)
    # args = {}
    # args.update(csrf(request))
    # args['todo'] = del_todolist
    del_todolist.delete()
    #return render_to_response('main.html', RequestContext(request))
    return redirect('/')



