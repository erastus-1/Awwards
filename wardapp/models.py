from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User 
from tinymce.models import HTMLField
# from django.utils import timezone
from django.db import models
import datetime as dt
import cloudinary

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = CloudinaryField('image', blank=True, null=True)
    bio = HTMLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return str(self.bio)


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


    @classmethod
    def update_bio(cls,id, bio):
        update_profile = cls.objects.filter(id = id).update(bio = bio,)
        return update_profile

    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile

class Project(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    image = CloudinaryField('image', blank=True, null=False)
    title = models.CharField(max_length=200)
    description = HTMLField(blank=True)
    link = models.URLField()
    date_created = models.DateTimeField(auto_now_add=True)

    def save_project(self):
        self.save()

    def __str__(self):
        return f'{self.author} post'

    def delete_project(self):
        self.delete()
