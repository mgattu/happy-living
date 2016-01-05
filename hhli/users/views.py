from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login 
from django.contrib.auth import logout
from django.contrib import messages

from .forms import LoginForm
from .forms import RegistrationForm

# Create your views here.
def index(request):
    return render_to_response('index.html')

def home(request):
    return render_to_response('home.html')

def user_landing_view(request):
    return render_to_response('landing.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            customer = authenticate(email=request.POST['email'], password=request.POST['password'])
            if customer is not None:
                if customer.is_active:
                    login(request, customer)
                    messages.error(request, "Login succesful")
                    return redirect('landing')
                else:
                    return redirect('home')
            else:
                messages.error(request, "Please Check Userid/password is wrong")
        else:
            pass

    else:
        form = LoginForm()

    return render(request, 'users/login_form.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print request.POST
        if form.is_valid():
            print "Good"        
    else:
        form = RegistrationForm()

    return render(request, 'users/registration_form.html', {'form': form})