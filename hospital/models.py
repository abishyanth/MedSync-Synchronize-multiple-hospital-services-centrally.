from django.db import models

# Create your models here.
class Hospital(models.Model):
    hname= models.CharField(max_length=100)
    image = models.CharField(max_length=255,null=True, blank=True)
    hcity = models.CharField(max_length=50)

    def __str__(self):
        return self.hname
    
class Department(models.Model):
    dname = models.CharField(max_length=50)
    d_loc= models.CharField(max_length=50)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.dname

class Doctor(models.Model):
    dname = models.CharField(max_length=50)
    dspecialization = models.CharField(max_length=50)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.dname
    
class Doctor_Profile(models.Model):
    dcontact= models.IntegerField()
    dage=models.IntegerField()
    dmail= models.EmailField()
    doctor=models.OneToOneField(Doctor,on_delete=models.CASCADE)

    def __str__(self):
        return self.doctor.dname

class Patient(models.Model):
    pname = models.CharField(max_length=50)
    page = models.IntegerField()
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.pname
    
class Patient_Profile(models.Model):
    pcontact= models.IntegerField()
    pmail= models.EmailField()
    p_address= models.CharField(max_length=100)
    patient=models.OneToOneField(Patient,on_delete=models.CASCADE)

    def __str__(self):
        return self.patient.pname
    
class Appointment(models.Model):
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patient.pname} - {self.doctor.dname} on {self.appointment_date} at {self.appointment_time}"
    
class Medical_Record(models.Model):
    record_date = models.DateField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Record for {self.patient.pname} by {self.doctor.dname} on {self.record_date}"