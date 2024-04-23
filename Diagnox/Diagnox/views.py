from accounts.models import Profile
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from .form import CancerPredictionForm
def acc(request):
    user_pk = request.session.get('userconn')  # Retrieve user's primary key from session
    if user_pk:
        try:
            user_conn = Profile.objects.get(pk=user_pk)  # Retrieve user object using primary key
        except Profile.DoesNotExist:
            user_conn = None
    else:
        user_conn = None
    return render(request, 'index.html', {'user_conn': user_conn})
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_v(request):
    logout(request)
    return redirect('/')  # Redirect to the desired page after logout (e.g., 'index.html')


def profile_picture_upload(request):
    if request.method == 'POST' and request.FILES['profile_picture']:
        profile_picture = request.FILES['profile_picture']
        # Retrieve the current user's profile
        user_profile = request.user.profile
        # Update the profile picture field with the uploaded file
        user_profile.img = profile_picture
        # Save the profile instance
        user_profile.save()
    return redirect('profile')  # Redirect back to the profile page




def formulaire(request):
    if request.method == 'POST':
        form = CancerPredictionForm(request.POST)
        if form.is_valid():
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            smoking = form.cleaned_data['smoking']
            yellow_fingers = form.cleaned_data['yellow_fingers']
            anxiety = form.cleaned_data['anxiety']
            peer_pressure = form.cleaned_data['peer_pressure']
            chronic_disease = form.cleaned_data['chronic_disease']
            fatigue = form.cleaned_data['fatigue']
            allergy = form.cleaned_data['allergy']
            wheezing = form.cleaned_data['wheezing']
            alcohol = form.cleaned_data['alcohol']
            coughing = form.cleaned_data['coughing']
            shortness_of_breath = form.cleaned_data['shortness_of_breath']
            swallowing_difficulty = form.cleaned_data['swallowing_difficulty']
            chest_pain = form.cleaned_data['chest_pain']
            print(gender)
            print(age)
            print(smoking)
            print(yellow_fingers)
            print(peer_pressure)
            print(chronic_disease)
            
            return redirect('/')  # Redirect to the desired page after form submission
    else:
        form = CancerPredictionForm()
    return render(request, 'form.html', {'form': form})
