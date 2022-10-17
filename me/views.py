from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Message
from .forms import MessageForm
from dashboard.models import GuestLocation, MyProject
from dashboard.utils import get_location


def my_portfolio(request):
    if 'ip_address' not in request.session and not request.user.is_superuser:
        guest_location_data = get_location()
        request.session['ip_address'] = guest_location_data

    request.session['has_message'] = False

    projects = MyProject.objects.all()

    context = {'form': 'form', 'projects': projects}
    return render(request, 'me/index.html', context)


def about(request):
    return render(request, 'me/about.html')


def contact(request):

    form = MessageForm()
    if request.method == 'POST':

        try:
            location = GuestLocation.objects.get(
                ip_address=request.session['ip_address'])
        except KeyError:
            location = None

        form = MessageForm(request.POST)
        if form.is_valid():
            form.send()
            request.session['has_message'] = True
            data = form.save(commit=False)
            data.message_location = location
            data.save()

        return redirect('contact')
    return render(request, 'me/contact.html')


def services(request):
    return render(request, 'me/services.html')


def single_project(request, title):
    title = title.replace('-', ' ')
    project = MyProject.objects.get(project_title=title)

    context = {'project': project}
    return render(request, 'me/single-project.html', context)
