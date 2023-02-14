from django.db import models

# Create your models here.
class Wish(models.Model):
    name = models.CharField(max_length=50,unique=True)
    message = models.CharField(max_length=100000,null=True)
    relation = models.CharField(max_length=1000,null=True)

class Gift(models.Model):
    name = models.CharField(max_length=50)
    emailed = models.IntegerField(default=0)
    gift = models.CharField(max_length=100000,null=True)
    email= models.EmailField(null=True)
    gifttype = models.CharField(max_length=1000,null=True)

class Video(models.Model):
    name = models.CharField(max_length=100,unique=True)
    url= models.URLField(max_length=100000,null=True)
    message = models.CharField(max_length=1000,null=True)

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, name):
        Video = cls(name=name)
        # do something with the Videos
        return Video
