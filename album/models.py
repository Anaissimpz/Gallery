from django.db import models
import datetime as dt


class Location(models.Model):
     country=models.CharField(max_length=50)
     city=models.CharField(max_length=50)
     place=models.CharField(max_length=50,default='unkown',null=True)
     def __str__(self):
        return self.country
     def save_location(self):
         self.save()
     def delete_location(self):
      self.delete()