from django.db import models

# Create your models here.
class Publisher(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=60)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    website=models.URLField()

    class meta:
        ordering=["-name"]

    def __str__(self):
        return self.name

class Author(models.Model):
    salutaion=models.CharField(max_length=10)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    headshot=models.ImageField(upload_to='author headshot')

    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=50)
    authors=models.ManyToManyField('Author',blank=True,null=True)
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)
    publication_date=models.DateField()

    def __str__(self):
        return self.title

