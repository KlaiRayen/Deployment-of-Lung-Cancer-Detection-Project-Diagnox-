from accounts.models import Profile
from django.shortcuts import render, redirect
from .forms import SignUpForm , SignInForm
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.files.storage import default_storage
from django.http import HttpResponseRedirect
from django.urls import reverse
def signin(request: HttpRequest):
    user_pk = request.session.get('userconn')
    if user_pk:
        try:
            user_conn = Profile.objects.get(pk=user_pk)  # Retrieve user object using primary key
        except Profile.DoesNotExist:
            user_conn = None
    else:
        user_conn = None
    if user_conn is not None:
        return redirect('/')  # Redirect to index if user is authenticated

    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                request.session['userconn'] = user.pk  # Store user's primary key in session
                return redirect('/')
    else:
        form = SignInForm()
    return render(request, 'front/login.html', {'form': form})

def signup(request):
    user_pk = request.session.get('userconn')
    if user_pk:
        try:
            user_conn = Profile.objects.get(pk=user_pk)  # Retrieve user object using primary key
        except Profile.DoesNotExist:
            user_conn = None
    else:
        user_conn = None
    if user_conn is not None:
        return redirect('/')  # Redirect to index if user is authenticated
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.instance.role = 'user'  # Replace 'Default Role' with your desired default value
            profile = form.save(commit=False)
            profile.set_password(form.cleaned_data['password'])
            profile.save()
            user = authenticate(request, email=profile.email, password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                # Redirect user to the home page or any other desired page
                return redirect('index')
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = SignUpForm()

    return render(request, 'front/signup.html', {'form': form})


def profile(request):
    user_pk = request.session.get('userconn')
    user_conn = None
    if user_pk:
        try:
            user_conn = Profile.objects.get(pk=user_pk)
        except Profile.DoesNotExist:
            pass
    
    if request.method == 'POST':
        if user_conn:
            user_conn.first_name = request.POST.get('first_name')
            user_conn.last_name = request.POST.get('last_name')
            user_conn.email = request.POST.get('email')
            profile_image = request.FILES.get('file2')  # Corrected name here
            if profile_image:
                user_conn.img = profile_image
            user_conn.save()
        return HttpResponseRedirect(reverse('profile'))

    return render(request, 'front/profile.html', {'user_conn': user_conn})

    return render(request, 'front/profile.html', {'user_conn': user_conn})
from django.contrib.auth.hashers import make_password

def password_change(request):
    user_pk = request.session.get('userconn')
    if user_pk:
        try:
            user_conn = Profile.objects.get(pk=user_pk)
        except Profile.DoesNotExist:
            user_conn = None
    else:
        user_conn = None    

    if request.method == 'POST':
        old_password = request.POST.get('oldpassword')
        new_password = request.POST.get('newpassword')
        confirm_password = request.POST.get('confirm_password')

        # Check if the old password matches the user's current password
        if user_conn and user_conn.check_password(old_password):
            # Check if the new password and the confirmed password match
            print(new_password)
            print(confirm_password)
            if new_password == confirm_password:
                # Set the new password for the user
                user_conn.password = make_password(new_password)
                user_conn.save()
                # Redirect to the profile page upon successful password change
                return HttpResponseRedirect(reverse('profile'))
            else:
                # Display an error message if the new password and the confirmed password do not match
                error_message = "New password and confirm password do not match."
        else:
            # Display an error message if the old password is incorrect
            error_message = "Incorrect old password."
        print(error_message)
        return render(request, 'front/password.html', {'user_conn': user_conn, 'error_message': error_message})

    return render(request, 'front/password.html', {'user_conn': user_conn})
