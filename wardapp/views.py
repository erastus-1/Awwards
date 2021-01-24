from .forms import *
from .models import *
from .models import  AwardMerch
from rest_framework import status
from .serializer import MerchSerializer
from rest_framework.views import APIView
from .permissions import IsAdminOrReadOnly
from rest_framework.response import Response
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    date = dt.date.today()
    projects = Projects.objects.all()

    return render(request,'all/home.html',locals())

@login_required(login_url='/accounts/login/')
def profile_info(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user).first()

    return render(request, 'profile/profile.html',locals())

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

class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = AwardMerch.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = MerchSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class MerchDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_merch(self, pk):
        try:
            return AwardMerch.objects.get(pk=pk)
        except MoringaMerch.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = MerchSerializer(merch)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = MerchSerializer(merch, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        merch = self.get_merch(pk)
        merch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
