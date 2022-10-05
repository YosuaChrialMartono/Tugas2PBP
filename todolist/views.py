from multiprocessing import context
from django.shortcuts import render
from todolist.models import Task, Task_Form
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user).values()
    context = {
        'item_todolist': data_todolist,
        'user': request.user.username,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)


def show_xml(request):
    data = Task.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = Task.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_json_by_id(request, id):
    data = Task.objects.filter(pk=id)
    # Jika JSON
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request, id):
    data = Task.objects.filter(pk=id)
    # Jika XML
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # melakukan login terlebih dahulu
            # membuat response
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            # membuat cookie last_login dan menambahkannya ke dalam response
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response


@login_required
def create_task(request):
    form = Task_Form(request.POST or None)
    if (form.is_valid and request.method == 'POST'):
        task_form = form.save(commit=False)
        task_form.user = request.user
        task_form.save()
        return redirect('/todolist/')
    response = {'form': Task_Form}
    return render(request, 'form.html', response)


def save_task(request):
    form = Task_Form(request.POST or None)
    if (form.is_valid and request.method == 'POST'):
        form.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
