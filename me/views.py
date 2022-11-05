from dashboard.models import GuestLocation, MyProject
from dashboard.utils import get_location
from django.shortcuts import redirect, render

from .forms import MessageForm


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


def single_project(request, slug):
    project = MyProject.objects.prefetch_related('project_image').get(slug=slug)
    print(project.tool)
    context = {'project': project}
    return render(request, 'me/single-project.html', context)
