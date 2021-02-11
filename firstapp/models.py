from django.db import models

# Create your models here.
class SignUp(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    User_Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=100)

class Bus(models.Model):
    Bus_Reg = models.CharField(max_length=100)
    Bus_Name = models.CharField(max_length=100)
    From = models.CharField(max_length=35)
    To = models.CharField(max_length=35)
    Dep_Time = models.CharField(max_length=100)
    Bus_Type = models.CharField(max_length=35)
    Bus_Class = models.CharField(max_length=35)
    Fare = int

class BusSeat(models.Model):
    Bus_Reg = models.ForeignKey(Bus, on_delete=models.CASCADE)
    Total_seat = int
    Seats_Name = models.CharField(max_length=200)

class Passenger(models.Model):
    User_Name = models.ForeignKey(SignUp, on_delete=models.CASCADE)
    Gender = models.CharField(max_length=35)
    Mob_Number = models.CharField(max_length=35)
    Payment_Type = models.CharField(max_length=35)
    Account_Number = models.CharField(max_length=100)

class Contact(models.Model):
    User_Name = models.ForeignKey(SignUp, on_delete=models.CASCADE)
    Subject = models.CharField(max_length=500)


