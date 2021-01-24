from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User 
from tinymce.models import HTMLField
from django.utils import timezone
from django.urls import reverse
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

    @classmethod
    def search_user(cls,user):
        return cls.objects.filter(user__username__icontains=user).all()

class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    image = CloudinaryField('image', blank=True, null=False)
    title = models.CharField(max_length=200)
    description = HTMLField(blank=True)
    link = models.URLField(max_length=70)
    post_date = models.DateTimeField(default=timezone.now)
    technologies = models.CharField(max_length=100)

    def save_project(self):
        self.save()

    def __str__(self):
        return f'{self.user} post'

    def delete_project(self):
        self.delete()

    @classmethod
    def search_projects(cls,search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project

class AwardMerch(models.Model):
    name = models.CharField(max_length=40)
    design = models.TextField()
    usability = models.TextField()
    content = models.TextField()