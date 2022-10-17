from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import GuestLocation, MyProject, ProjectImage, ProjectTool
from .forms import MyProjectForm
from me.models import Message
from .serializer import GuestLocationSerializer
from .decorators import admin_only
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@login_required(login_url='login')
def dashboard(request):
    visitors = GuestLocation.objects.all()
    messages = Message.objects.all()

    context = {'messages': messages, 'visitors': visitors, }
    return render(request, 'dashboard/dashboard.html', context)


@login_required(login_url='login')
def manage_projects(request):
    projects = MyProject.objects.all()

    context = {'projects': projects}
    return render(request, 'dashboard/manage-projects.html', context)


@login_required(login_url='login')
@admin_only
def add_project(request):
    form = MyProjectForm()
    if request.method == 'POST':
        form = MyProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('man_pro')

    context = {'form': form}
    return render(request, 'dashboard/add-project.html', context)


@login_required(login_url='login')
@admin_only
def add_images_and_tools(request):
    if request.method == 'POST':
        if 'tool' in request.POST:
            ProjectTool.objects.create(
                name=request.POST.get('tool')
            )
        elif 'image' in request.POST:
            ProjectImage.objects.create(
                name=request.POST.get('name'),
                image=request.POST.get('image'),
                order=request.POST.get('order'),
            )
        return redirect('addImgTool')

    return render(request, 'dashboard/add-images&tools.html')


@login_required(login_url='login')
@admin_only
def update_project(request, pk):
    project = MyProject.objects.get(id=pk)
    form = MyProjectForm(instance=project)
    if request.method == 'POST':
        form = MyProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('man_pro')

    context = {'form': form, 'project': project}
    return render(request, 'dashboard/update-project.html', context)


@login_required(login_url='login')
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
