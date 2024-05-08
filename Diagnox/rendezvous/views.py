from accounts.models import Profile
from django.shortcuts import render, redirect
from .forms import RendezvousForm
from datetime import datetime, timedelta, time
from rendezvous.models import Rendezvous
from django.http import JsonResponse
import logging


# Create your views here.
def listDoc(request):
    user_pk = request.session.get('userconn')  # Retrieve user's primary key from session
    if user_pk:
        try:
            user_conn = Profile.objects.get(pk=user_pk)  # Retrieve user object using primary key
        except Profile.DoesNotExist:
            user_conn = None
    else:
        user_conn = None
    doctors = Profile.objects.filter(role='doctor')
    return render(request, 'rendezvous/listdoc.html', {'user_conn': user_conn , 'doctors' : doctors})

# Create your views here.
def showListDocRdv(request):
    user_pk = request.session.get('userconn')  # Retrieve user's primary key from session
    if user_pk:
        try:
            user_conn = Profile.objects.get(pk=user_pk)  # Retrieve user object using primary key
        except Profile.DoesNotExist:
            user_conn = None
    else:
        user_conn = None
    doctors = Profile.objects.filter(role='doctor')
    return render(request, 'rendezvous/doctorrdv.html', {'user_conn': user_conn})

# Create your views here.
def listDocRdv(request):
    logger = logging.getLogger(__name__)
    user_pk = request.session.get('userconn')  # Retrieve user's primary key from session
    logger.warning("user_pk")
    logger.warning(user_pk)
    logger.warning(user_pk)
    if user_pk:
        try:
            user_conn = Profile.objects.get(pk=user_pk)  # Retrieve user object using primary key
            if user_conn.is_doctor:
                rdvs = Rendezvous.objects.filter(doctor_id=user_pk).select_related('client').select_related('doctor')

                result = [{
                    "id": rdv.id,
                    "date": rdv.date,
                    "client_id": rdv.client.id,
                    "client_first_name": rdv.client.first_name,  # Assuming email is a field in Profile model
                    "client_last_name": rdv.client.last_name,  # Assuming email is a field in Profile model
                    "client_email": rdv.client.email,  # Assuming email is a field in Profile model
                    "doctor_id": rdv.doctor_id,
                    "doctor_first_name": rdv.doctor.first_name,  # Assuming email is a field in Profile model
                    "doctor_last_name": rdv.doctor.last_name,  # Assuming email is a field in Profile model
                    "etat": rdv.etat,
                    "note": rdv.note
                } for rdv in rdvs]

                return JsonResponse({'doctorRdv': list(result)})

        except Profile.DoesNotExist:
            return JsonResponse({'doctorRdv': []})
    else:
        return JsonResponse({'doctorRdv': []})

def fetch_time_slots(request):
    logger = logging.getLogger(__name__)

    search_date = request.GET.get('date')

    search_start_time = datetime.strptime(request.GET.get('start_time'), '%H:%M')
    search_end_time = datetime.strptime(request.GET.get('end_time'), '%H:%M')
    search_doctor_id = request.GET.get('doctor_id')
    logger.warning("search_doctor_id")
    logger.warning(search_doctor_id)
    search_doctor = Profile.objects.get(pk=search_doctor_id)

    rdvs = Rendezvous.objects.filter(date__date=search_date, date__time__range=(search_start_time, search_end_time), doctor_id=search_doctor_id)

    found_dates = []
    logger.warning(search_date)
    logger.warning(rdvs)
    logger.warning(rdvs.count())

    for r in rdvs:
        found_dates.append(r.date.time())
    logger.warning("xxxxxxxxxxxxxxxxxxxx")
    logger.warning(found_dates)
    time_slots = []
    current_time = search_start_time

    while current_time <= search_end_time:
        next_time = current_time + timedelta(minutes=30)
        logger.warning(current_time)
        if current_time.time() not in found_dates:
            time_slots.append({
                "value" : current_time.strftime('%H:%M'),
                "range" : current_time.strftime('%H:%M') + " - " + next_time.strftime('%H:%M')
                })
        current_time = next_time
    logger.warning("time_slots")
    logger.warning(time_slots)

    return JsonResponse({'time_slots': time_slots})

def create_rendezvous(request, doctor_id):
    user_pk = request.session.get('userconn')  # Retrieve user's primary key from session
    if user_pk:
        try:
            user_conn = Profile.objects.get(pk=user_pk)  # Retrieve user object using primary key
        except Profile.DoesNotExist:
            user_conn = None
    else:
        user_conn = None
    doctor = Profile.objects.get(pk=doctor_id)
    if request.method == 'POST':
        form = RendezvousForm(request.POST)
        if form.is_valid():
            rendezvous = form.save(commit=False)
            rendezvous.doctor = doctor
            rendezvous.client = user_conn
            rendezvous.save()
            return redirect('/')  # Redirect to a success page
    else:
        form = RendezvousForm()
    return render(request, 'rendezvous/form.html', {'form': form , 'doctor_id':doctor_id, 'user_conn': user_conn})


def listRndv(request):
    return render(request, 'doctor/form.html', {'form': form , 'user_conn': user_conn})
