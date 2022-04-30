from django.db import models

# Create your models here.
class Pro(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Category(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField()
    def __str__(self):
        return self.title

class Plantes(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    img = models.ImageField(upload_to='images')
    date=models.DateTimeField()
    cat= models.ForeignKey(Category,on_delete=models.CASCADE)
     
    def __str__(self):
        return self.name

class Plants(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    img = models.ImageField(upload_to='images')
    price = models.IntegerField()
    date=models.DateTimeField()
    cat= models.ForeignKey(Category,on_delete=models.CASCADE)
     
    def __str__(self):
        return self.name


class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name

