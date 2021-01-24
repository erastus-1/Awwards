from . views import PostDetailView, PostCreateView,home
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url('profile/',views.profile_info, name='profile'),
    url('search/', views.search, name='search'),
    url('update/',views.profile_update, name='update'),
    url('post_detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    url('post_edit/', PostCreateView.as_view(), name='post_create'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
