from django.contrib.auth.models import User
from django.test import TestCase
from .models import *


# Create your tests here.
class ProfileTestClass(TestCase):
    '''
    test class for profile class
    '''

    def setUp(self):
        self.new_user = User(username='test', email='test@gmail.com', password='2345')
        self.new_user.save()
        self.new_profile = Profile(image='image.jpg', bio='testbio', contact='pretence47484.com', user=self.new_user)


    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_method(self):
        self.new_profile.save_profile()
        profile =Profile.objects.all()
        self.assertTrue(len(profile)>0)

    def test_delete_method(self):
        self.new_profile.save_profile()
        self.new_profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)==0)
        