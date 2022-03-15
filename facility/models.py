from django.db import models


class FacilityType(models.Model):
    facility_name = models.CharField(max_length=100, primary_key=True)


class Facility(models.Model):
    STATUS_CHOICE = [('Approved', 'Approved'), ('Pending', 'Pending')]

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, blank=True, null=True)
    number_of_medical_doctor = models.IntegerField(blank=True, null=True)
    number_of_nurse = models.IntegerField(blank=True, null=True)
    number_of_midwife = models.IntegerField(blank=True, null=True)
    facility_types = models.ManyToManyField('FacilityType')
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='Pending')
