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
        self.new_profile = Profile(image='image.jpg', bio='testbio', user=self.new_user)


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
        

class ProjectTestClass(TestCase):

    def setUp(self):        
        self.new_user = User(username='test', email='test@gmail.com', password='1234')
        self.new_user.save()
        self.new_project = Project(title="test1",image='test.png',description="This is a personal test.",author=self.new_author, link="https://github.com/test1/tests")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_project,Project))    

    def test_save_project(self):
        self.new_project.save_project()
        project = project.objects.all()
        self.assertTrue(len(project)>0)

    def test_delete_project(self):
        self.new_project.save_p()
        self.new_project.delete_project()
        project = project.objects.all()
        self.assertTrue(len(project)==0)