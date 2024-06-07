from django.shortcuts import render, redirect
from authors import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import login, logout, authenticate,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.models import Post

def register(request):
    if request.method == "POST":
        registerForm = forms.RegitrationForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            messages.success(request, 'Account created successfully')
            return redirect('userLogin')
    else:
        registerForm= forms.RegitrationForm()
    return render(request,  'register.html', {'form':registerForm, 'type': 'Register'})

def userLogin(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is None:
                pass
            else:
                print("Success")
                login(request, user)
                messages.success(request, 'Logged in  successfully')
                return redirect('profile')
        else:
            messages.success(request, 'No user found')
    else:
        form = AuthenticationForm()
    return render(request, 'register.html', {'form': form, 'type':'Login'})

@login_required(login_url="/author/login/")
def profile(request):
    data  =Post.objects.filter(author = request.user)
    return render(request,  'profile.html', {'data': data})
 
 
@login_required(login_url="/author/login/")
def update_profile(request):
    if request.method == "POST":
            profile_form = forms.ChangeUserDataForm(request.POST, instance=request.user)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Account Updated successfully')
                return redirect('profile')
    else:
        profile_form= forms.ChangeUserDataForm(instance=request.user)
    return render(request,  'update_profile.html', {'form':profile_form})
 

def userLogout(request):
    logout(request)
    return redirect('userLogin')

@login_required(login_url='/author/login/')
def password_change(request):
    if request.method == "POST":
        pass_change_form = PasswordChangeForm(request.user,data=request.POST)
        if pass_change_form.is_valid():
            pass_change_form.save()
            messages.success(request, 'Password changed successfully')
            update_session_auth_hash(request, pass_change_form.user)
            return redirect('profile')
    else:
        pass_change_form= PasswordChangeForm(request.user)
    return render(request,  'password_change.html', {'form':pass_change_form})
