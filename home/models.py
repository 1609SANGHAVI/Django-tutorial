from django.db import models

# Create your models here.

class Color(models.Model):
    color_name=models.CharField(max_length=100)

    def __str__(self)->str:
        return self.color_name
    
class UserDetails(models.Model):
    color=models.ForeignKey(Color,null=True,blank=True,on_delete=models.CASCADE,related_name="color")
    name=models.CharField(max_length=1000)
    age = models.IntegerField()  
    email = models.EmailField()
   
class Restaurant(models.Model):
    name = models.CharField(max_length=255, default='Unknown')
    address = models.CharField(max_length=255, default='Unknown')
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class LoginEntry(models.Model):
    class Meta:
        verbose_name = "Login"
        verbose_name_plural = "Login"
        managed = False  # No DB table will be created

class Blog(models.Model):
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        managed = False

    def __str__(self):
        return "Blog"

       