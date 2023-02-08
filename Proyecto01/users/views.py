from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from users.forms import RegisterForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from users.models import UserProfile

def login_view(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, 'users/login.html', context=context)

    elif request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('/')
                
        form = AuthenticationForm()
        context = {
            'form': form,
            'errors':'Usuario o contraseña incorrectos!'
        }
        return render(request, 'users/login.html', context=context)

def signup_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        context = {
            'form': form,
        }
        return render(request, 'users/signup.html', context=context)
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            return redirect('login')
        context = {            
            'errors':form.errors,
            'form':RegisterForm(),
            
        }
        return render(request, 'users/signup.html', context=context)

@login_required
def profile_view(request):
    user = request.user
    if request.method == 'GET':
        context = {
            'phone': user.profile.phone,
            'birth_date': user.profile.birth_date,
            'profile_image': user.profile.profile_image,
        }
        return render(request, 'users/profile.html', context=context)

@login_required
def update_user_profile(request):
    user = request.user
    if request.method == 'GET':
        form = UserProfileForm(initial={
            'phone':request.user.profile.phone,
            'birth_date':request.user.profile.birth_date,
            'profile_image':request.user.profile.profile_image
        })
        context ={
            'form':form
        }
        return render(request, 'users/update_profile.html', context=context)

    elif request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.profile_image = form.cleaned_data.get('profile_image')
            user.profile.save()
            return redirect('index')
        
        context = {
            'errors':form.errors,
            'form':UserProfileForm()
        }
        return render(request, 'users/update_profile.html', context=context)