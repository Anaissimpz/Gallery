from django.db import models
import datetime as dt


class Location(models.Model):
    country=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    place=models.CharField(max_length=20,default='unkown',null=True)
    def __str__(self):
        return self.country
    def save_location(self):
        self.save()
    def delete_location(self):
        self.delete()
    @classmethod
    def update_all(cls,id,new,newer,newest):
        location=Location.objects.filter(id=id)
        location.update(country=new,city=newer,place=newest)
        return location

class Category(models.Model):
     category=models.CharField(max_length=50)
     def __str__(self):
        return self.category

     def save_category(self):
         self.save()

     def delete_category(self):
      self.delete()

     @classmethod
     def update_name(cls,id,new):
      caty=Category.objects.filter(id=id)
      caty.update(category=new)
      return caty