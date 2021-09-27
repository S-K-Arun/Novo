from django.db import models

class Movie(models.Model):
    Name = models.CharField(max_length=200)
    featured_image=models.ImageField(null=True,blank=True,default='SK_custom.jpg')
    
    def __str__(self):
        return self.Name

class Academi(models.Model):
    Name = models.CharField(max_length=200)
    featured_image=models.ImageField(null=True,blank=True,default='SK_custom.jpg')
    
    def __str__(self):
        return self.Name

        
class Art(models.Model):
    Name = models.CharField(max_length=200)
    featured_image=models.ImageField(null=True,blank=True,default='SK_custom.jpg')
    
    def __str__(self):
        return self.Name

class Buildings(models.Model):
    Name = models.CharField(max_length=200)
    featured_image=models.ImageField(null=True,blank=True,default='SK_custom.jpg')
    
    def __str__(self):
        return self.Name

class Cars(models.Model):
    Name = models.CharField(max_length=200)
    featured_image=models.ImageField(null=True,blank=True,default='SK_custom.jpg')
    
    def __str__(self):
        return self.Name


class upload(models.Model):
    Name = models.CharField(max_length=200)
    featured_image=models.ImageField(upload_to="static/images")

    def __str__(self):
        return self.Name
    
