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
      
class Image(models.Model):
    image=models.ImageField(upload_to = 'images/')
    name= models.CharField(max_length =30)
    description=models.TextField()
    location=models.ForeignKey(Location,null=True)
    category=models.ForeignKey(Category, null=True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

    def save_image(self):
         self.save()
    def delete_image(self):
      self.delete()
    @classmethod
    def share(cls,id):
      image=Image.objects.filter(id=id)
      self.pyperclip.copy(image.image.cdn_url)

    @classmethod
    def get_image(cls,id):

      pictures =Image.objects.filter(id=id)
      return pictures 
    @classmethod
    def get_category_images(cls,caty):
      cate=Category.objects.filter(category=caty).first()
      images=Image.objects.filter(category=cate)
      return images
    @classmethod
    def get_location_images(cls,loc):
      lolo=Location.objects.filter(pk=loc)
      images=Image.objects.filter(location=lolo)
      return images

    @classmethod
    def search_by_name(cls,search_term):
        images = cls.objects.filter(category__icontains=search_term)
        return images

    @classmethod
    def update_name(cls,id,new):
      image=Image.objects.filter(id=id)
      image.update(name=new)
      return image
    @classmethod
    def search_by_category(cls,search_term):
      image_location = Location.objects.filter(location__country__icontains=search_term)
      return image_location