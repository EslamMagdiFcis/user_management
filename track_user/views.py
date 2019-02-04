from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import UserCreationForm


def home(request):
    return render(request=request, template_name='track_user/home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request=request, template_name='registration/signup.html', context={'form': form})


@login_required
def profile_view(request):
    user = request.user
    return render(request, 'registration/profile.html', {'user': user})


@login_required
def user_resources(request):
    host = request.META['SERVER_NAME']
    port = request.META['SERVER_PORT']
    mobile = request.user_agent.is_mobile
    pc = request.user_agent.is_pc
    browser = request.user_agent.browser
    os = request.user_agent.os
    device = request.user_agent.device

    return render(request, 'track_user/user_resources.html',
                  {'host': host, 'port': port, 'mobile': mobile, 'pc': pc,
                   'os': os, 'browser': browser, 'device': device})
