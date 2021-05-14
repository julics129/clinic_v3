from django.db import models

# Create your models here.
class appointment(models.Model):
	app_id = models.AutoField(primary_key=True)
	PatientName= models.CharField(max_length=30)
	PatientEmail= models.EmailField(max_length=30)
	PatientPhone= models.CharField(max_length=13)
	AppointmentDate=models.DateField()
	doc_id=models.ForeignKey('department', on_delete=models.CASCADE)
	Message=models.CharField(max_length=70)
	def __str__(self):
		return self.PatientName
	
class contact(models.Model):
	Name=models.CharField(max_length=30)
	Email=models.EmailField(max_length=30)
	Subject=models.CharField(max_length=30)
	Message=models.CharField(max_length=70)
	
class department(models.Model):
	department_name=models.CharField(max_length=30)
	doctor_name=models.CharField(max_length=30)
	doc_id = models.AutoField(primary_key=True)
	
	def __str__(self):
		return self.doctor_name

	
class prescription(models.Model):
	pres_id=models.AutoField(primary_key=True)
	app_id=models.ForeignKey('appointment', on_delete=models.CASCADE)
	medicines =models.CharField(max_length=30)
	def __str__(self):
		return self.app_id.PatientName