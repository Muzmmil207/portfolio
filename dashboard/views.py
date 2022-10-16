from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .models import GuestLocation, MyProject
from .forms import AboutProjectsForm
from me.models import Message
from me.forms import MessageForm
from .serializer import GuestLocationSerializer
from .decorators import admin_only
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@login_required(login_url='login')
def dashboard(request):
    # print(request.headers)
    visitors = GuestLocation.objects.all()
    print(len(GuestLocation.objects.all()))
    messages = Message.objects.all()
    context = {'messages': messages, 'visitors': visitors, }
    return render(request, 'dashboard/dashboard.html', context)


@login_required(login_url='login')
def manage_projects(request):
    projects = MyProject.objects.all()
    form = AboutProjectsForm()
    if request.method == 'POST':
        form = AboutProjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('man_pro')
    context = {'form': form, 'projects': projects}

    return render(request, 'dashboard/manage-projects.html', context)


@admin_only
def add_project(request):
    page_name = 'add'
    form = AboutProjectsForm()
    if request.method == 'POST':
        form = AboutProjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('man_pro')
    context = {'form': form, 'page_name': page_name}
    return render(request, 'dashboard/add-project.html', context)


@admin_only
def update_project(request, pk):
    page_name = 'update'
    project = MyProject.objects.get(id=pk)
    form = AboutProjectsForm(instance=project)
    if request.method == 'POST':
        form = AboutProjectsForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('man_pro')
    context = {'form': form, 'project': project, 'page_name': page_name}
    return render(request, 'dashboard/update-project.html', context)


@admin_only
def delete_project(request, pk):
    try:
        project = MyProject.objects.get(id=pk)
        project.delete()
        return redirect('man_pro')
    except:
        return HttpResponse('Page not found (404)')


def login_user(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        try:
            User.objects.get(username=username)
        except:
            messages.error(request, 'User dose not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'User name or password is incorrect')

    return render(request, 'dashboard/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_view(request):

    product = GuestLocation.objects.all()
    serializer = GuestLocationSerializer(product, many=True)

    return Response(serializer.data)
