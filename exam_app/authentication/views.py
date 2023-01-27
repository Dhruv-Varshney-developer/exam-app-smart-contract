
from django.shortcuts import render, redirect
from .forms import RegisterForm,answerspace
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from .smart_contract_integration import questionextract
import time



# Create your views here.
@login_required(login_url="/login")
def home(request):
    return render(request, 'authentication/home.html')

@login_required(login_url="/login")
def question(request):
    title=None
    if request.method == 'POST':
        title = questionextract().x
        print(title)
        form = answerspace(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.save()
            return redirect("/home")
    else:
        title = questionextract().x
        print(title)
        form = answerspace()

    return render(request, 'authentication/question_page.html', {"Question":title,"form": form})

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})
