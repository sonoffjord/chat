from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import SignUpForm


def frontpage(request):
    return render(request, 'chat/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')
    else:
        form = SignUpForm()

    return render(request, 'chat/form.html', {'form': form})


