from .forms import *
from .models import *
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView


# Create your views here.
def home(request):
    date = dt.date.today()
    projects = Projects.objects.all()

    return render(request,'all/home.html',locals())

@login_required(login_url='/accounts/login/')
def profile_info(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user).first()

    return render(request, 'profile/profile.html', {'profile':profile})

@login_required(login_url='/accounts/login/')
def profile_update(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.user = current_user
            add.save()
        return redirect('profile')

    else: 
        form = UpdateForm()
    return render(request, 'profile/update.html',{'form':form})


# @login_required(login_url='/accounts/login/')
# def post_edit(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = ProjectForm(request.POST, request.FILES)
#         if form.is_valid():
#             add=form.save(commit=False)
#             add.author = current_user
#             add.save()
#             return redirect('post_edit.html')

#     else:
#             form = ProjectForm()
#             return render(request,'post_edit.html', {"form":form})

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['image', 'title', 'description', 'link','technologies', 'post_date', 'user']
    template_name = 'post_edit.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)