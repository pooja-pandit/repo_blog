from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify








class Topic(models.Model):
    name=models.CharField(max_length=255)
    slug = models.SlugField(unique=True,blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Topic, self).save(*args, **kwargs)




class Category(models.Model):
    name=models.CharField(max_length=50)


    def __str__(self):
        return self.name

class Blog(models.Model):
    header=models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    category= models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    topics = models.ManyToManyField(Topic, blank=True)
    img=models.ImageField(upload_to='blog_img',null=True)
    subheader=models.CharField(max_length=255)
    details=models.TextField()
    pub_date=models.DateField(auto_now_add=True)
    likes=models.IntegerField(default=0)


    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


    def __str__(self):
        return self.header

class Comment(models.Model):
    blogs=models.ForeignKey(Blog,on_delete=models.SET_NULL,related_name="comments",null=True)
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    text=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    approved_comment=models.BooleanField(default=False)

    def approve(self):
        self.approved_comment=True
        self.save()


    def __str__(self):
        return self.text






