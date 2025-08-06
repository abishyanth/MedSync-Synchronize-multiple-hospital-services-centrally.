from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from hospital.models import Hospital, Department, Doctor, Doctor_Profile, Patient


from django.contrib.auth.models import User, Group

def signup_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        role = request.POST.get('role').lower()
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if User.objects.filter(username=username).exists():
                context['error'] = "Username already exists."
            else:
                user = User.objects.create_user(username=username, email=email, password=password)

                # Create the group if it doesn't exist
                group, created = Group.objects.get_or_create(name=role)
                user.groups.add(group)

                user.save()
                request.session['user_role'] = role
                return redirect('authentication:login_view')
        else:
            context['error'] = "Passwords do not match."
    return render(request, 'signup.html', context)



def login_view(request):
    role = request.session.get('user_role', 'User')  
    context = {
        'role': role
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password) 

        if user is not None:
            login(request, user)
            return redirect('hospital:hospitals')
        context['error'] = 'Invalid Credentials!!'

    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('authentication:login_view')