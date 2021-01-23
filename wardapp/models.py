from cloudinary.models import CloudinaryField
from djando.contrib.auth.models import User 
from tinymce.models import HTMLFIELD
from django.utils import timezone
from django.db import models
import cloudinary

# Create your models here.
class Profile(models.Model):
    user = modles.OneToOneField(User, ond_delete=models.CASCADE, primary_key=True)
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
    