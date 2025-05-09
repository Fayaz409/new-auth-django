from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
from .forms import UserForm


def home(request):
    return render(request,'authapp/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserForm(data = request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form = UserForm()
    return render(request,'authapp/signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
              return render(request,'authapp/not_found.html')
    else:
        form=AuthenticationForm()
    return render(request,'authapp/login.html',{'form':form})

    