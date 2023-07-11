from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.

def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'signupaccount.html',
            {'form': UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],
                    password= request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request,'signupaccount.html',
                    {
                        'form':UserCreateForm,
                        'error':'Username already taken. Choose new username.'
                    }
                    )
        else:
            return render(request, 'signupaccount.html',
                {'form':UserCreateForm, 'error':'Passwords do not match'})

@login_required
def logoutaccount(request):
    logout(request)
    return redirect('home')

def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'loginaccount.html',
            {'form':AuthenticationForm})
    else:
        username=request.POST['username']
        user = authenticate(request,
            username=username,
            password=request.POST['password']
        )
        if user is None:
            return render(request,'loginaccount.html',
                    {
                        'form': AuthenticationForm(),
                        'error': f'username({username}) and password do not match'
                    }
                )
        else:
            login(request,user)
            return redirect('home')


@login_required
def view_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    # if request.user != user:
    #     return redirect('home')  # Redirect to home page if the current user is not the profile owner

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('view_profile', user_id=user.id)
    else:
        form = UserProfileForm(instance=user.userprofile)

    return render(request, 'profile.html', {'profile_user': user, 'form': form})
