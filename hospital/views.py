from django.shortcuts import render,get_object_or_404,redirect
from .models import Hospital,Department,Doctor,Doctor_Profile,Patient,Patient_Profile,Appointment
# Create your views here.
def main(request):
    return render(request, 'main.html')

def hospitals(request):
    hospitals = Hospital.objects.all()
    return render(request, 'hospital.html', {'hospitals': hospitals})

def hospital_detail_view(request, hospital_id):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    
    user = request.user
    is_doctor = user.groups.filter(name='doctor').exists()
    is_patient = user.groups.filter(name='patient').exists()

    context = {
        'hospital': hospital,
        'is_doctor': is_doctor,
        'is_patient': is_patient,
    }

    return render(request, 'hospital_detail_view.html', context)

def add_hospital(request):
    if request.method == 'POST':
        hname = request.POST.get('hname')
        image = request.POST.get('image')
        hcity = request.POST.get('hcity')
        Hospital.objects.create(
            hname=hname, 
            image=image,
            hcity=hcity
        )
        return redirect('hospitals')
    return render(request, 'hospital_create.html')

def add_Department(request, hospital_id):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    if request.method == 'POST':
        dname = request.POST.get('dname')
        d_loc = request.POST.get('d_loc')
        Department.objects.create(
            dname=dname, 
            d_loc=d_loc, 
            hospital=hospital
        )
        return redirect('hospital_detail', hospital_id=hospital.id)
    context= {
        'hospital': hospital
    }
    return render(request, 'add_department.html', context)

def add_docotor(request, hospital_id):
    hospital= get_object_or_404(Hospital, id=hospital_id)
    if request.method == 'POST':
        dname = request.POST.get('dname')
        dspecialization = request.POST.get('dspecialization')
        dcontact = request.POST.get('dcontact')
        dage = request.POST.get('dage')
        dmail = request.POST.get('dmail')
        dname = Doctor.objects.create(
            dname=dname, 
            dspecialization=dspecialization,
            Department=hospital.department_set.first()
        )
        Doctor_Profile.objects.create(
            doctor=dname, 
            dcontact=dcontact, 
            dage=dage, 
            dmail=dmail
        )
        return redirect('hospital:doctor_list', hospital_id=hospital.id)

    context={
        'hospital': hospital
    }
    return render(request, 'add_doctor.html', context)

def doctor_list_view(request, hospital_id):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    doctors = Doctor.objects.filter(Department__hospital=hospital)
    context={
        'hospital': hospital,
        'doctors': doctors
    }
    return render(request, 'doctor_list.html', context)

def add_patient(request, doctor_id):
    if request.method == 'POST':
        pname = request.POST.get('pname')
        page = request.POST.get('page')
        pcontact = request.POST.get('pcontact')
        pmail = request.POST.get('pmail')
        p_address = request.POST.get('p_address')
        
        doctor = get_object_or_404(Doctor, id=doctor_id)
        patient = Patient.objects.create(
            pname=pname, 
            page=page, 
            Doctor=doctor
        )
        Patient_Profile.objects.create(
            patient=patient, 
            pcontact=pcontact, 
            pmail=pmail, 
            p_address=p_address
        )
        return redirect('hospital:patient_list', hospital_id=doctor.Department.hospital.id)
    return render(request, 'add_patient.html', {'doctor_id': doctor_id})

def patient_list_view(request, hospital_id):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    patients = Patient.objects.filter(Doctor__Department__hospital=hospital)
    context={
        'hospital': hospital,
        'patients': patients
    }
    return render(request, 'patient_list.html', context)

def patient_profile_view(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    try:
        profile = patient.patient_profile
    except Patient_Profile.DoesNotExist:
        profile = None
    context={
        'patient': patient,
        'profile': profile
    }
    return render(request, 'patient_profile.html', context)

def doctor_profile_view(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    patients = Patient.objects.filter(Doctor=doctor)
    try:
        profile = doctor.doctor_profile
    except Doctor_Profile.DoesNotExist:
        profile = None
    context={
        'doctor': doctor,
        'profile': profile,
        'patients': patients,
    }
    return render(request, 'doctor_profile.html', context)

def remove_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    hospital_id = patient.Doctor.Department.hospital.id
    patient.delete()
    return redirect('hospital:patient_list', hospital_id=hospital_id)