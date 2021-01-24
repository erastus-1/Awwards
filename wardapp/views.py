from .forms import *
from .models import *
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


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

@login_required(login_url='/accounts/login/')
def search(request):
    profiles = User.objects.all()

    if 'username' in request.GET and request.GET['username']:
        search_term = request.GET.get('username')
        results = User.objects.filter(username__icontains=search_term)
        message = f'{search_term}'
        profile_pic = User.objects.all()

        return render(request,'all/results.html',locals())

    return redirect('home')


@login_required(login_url='/accounts/login/')
def post_edit(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.author = current_user
            add.save()
            return redirect('home')

    else:
            form = ProjectForm()
            return render(request,'all/post_edit.html', {"form":form})


@login_required(login_url='/accounts/login/')
def get_project(request, id):
    project = Projects.objects.get(pk=id)

    return render(request, 'all/post_detail.html', {'project':project})

