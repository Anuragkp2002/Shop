from django.db import models

class Register_tb(models.Model):
    Name=models.CharField(max_length=20)
    Address=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
class image_tb(models.Model):
    File=models.FileField()    
class country_tb(models.Model):
    Name=models.CharField(max_length=20)
class state_tb(models.Model):
    Name=models.CharField(max_length=20)
    countryid=models.ForeignKey(country_tb,on_delete=models.CASCADE)   

    
