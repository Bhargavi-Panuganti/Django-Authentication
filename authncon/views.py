from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
# Create your views here.
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from authncon.forms import create
from django.contrib import messages
def Register(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return HttpResponse('Success')
    return render(request,'register.html',{'form':form})
def loginv(request):
    form = AuthenticationForm(request, data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('Logged In Successfully..')
            else:
                return HttpResponse('Invalid credentials')
    return render(request, 'login.html', {'form': form})
     
def dashboard(request):
    return render(request,'dashboard.html')
def logoutv(request):
    logout(request)
    return redirect('login')