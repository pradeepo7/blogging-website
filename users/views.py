from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import Userregisterform , ProfileUpdateForm ,UserUpdateForm
from django.contrib.auth import decorators
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = Userregisterform(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            messages.success(request, ' you succesfully created user {} !'.format(username))
            return redirect('login')
    else:
        form = Userregisterform()
    return render(request,'users/register.html',{'form':form})



@decorators.login_required
def profile(request):

    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            username = request.POST['username']
            messages.success(request, ' you username {} and profile photo sucessfully updated !'.format(username))
            return redirect('profile')


    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = UserUpdateForm(instance=request.user)


    context = {
        "p_form" : p_form,
        "u_form" : u_form
    }
    return render(request,'users/profile.html',context)

def delete_user(self):
    self.user.delete()
    return redirect('login')
    