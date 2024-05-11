from accounts.models import Profile
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from .form import CancerPredictionForm
from tensorflow.keras.models import load_model
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re
import random
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.preprocessing import LabelEncoder
import pandas as pd 
import json
from django.http import JsonResponse
import os
from django.conf import settings

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





# Load your data outside of the view function
with open(os.path.join(settings.STATICFILES_DIRS[0], 'intents.json'), 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data['intents'])
dic = {"tag":[], "patterns":[], "responses":[]}
for i in range(len(df)):
    ptrns = df[df.index == i]['patterns'].values[0]
    rspns = df[df.index == i]['responses'].values[0]
    tag = df[df.index == i]['tag'].values[0]
    for j in range(len(ptrns)):
        dic['tag'].append(tag)
        dic['patterns'].append(ptrns[j])
        dic['responses'].append(rspns)
        
df = pd.DataFrame.from_dict(dic)
df['tag'].unique()


# Load your tokenizer
tokenizer = Tokenizer(lower=True, split=' ')
tokenizer.fit_on_texts(df['patterns'])
model_file_path = os.path.join(settings.STATICFILES_DIRS[0], 'model.h5')
model = load_model(model_file_path)
ptrn2seq = tokenizer.texts_to_sequences(df['patterns'])
X = pad_sequences(ptrn2seq, padding='post')
lbl_enc = LabelEncoder()
y = lbl_enc.fit_transform(df['tag'])
# Define your chatpal view
def generate_answer(pattern, model, tokenizer, data):
    text = [pattern.lower()]
    x_test = tokenizer.texts_to_sequences(text)

    x_test = pad_sequences(x_test, padding='post', maxlen=X.shape[1]) 
    y_pred = model.predict(x_test)
    y_pred = y_pred.argmax()
    tag = lbl_enc.inverse_transform([y_pred])[0]
    intents_df = pd.DataFrame(data['intents'])
    responses = intents_df[intents_df['tag'] == tag]['responses'].values[0]
    return random.choice(responses)

def chatpal(request):
    user_pk = request.session.get('userconn')
    if user_pk:
        try:
            user_conn = Profile.objects.get(pk=user_pk)
        except Profile.DoesNotExist:
            user_conn = None
    else:
        user_conn = None   

    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        response = generate_answer(user_input, model, tokenizer, data)
        return JsonResponse({'response': response})
    else:
        return render(request, 'front/chatpal.html', {'user_conn': user_conn})