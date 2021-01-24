from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url('profile/',views.profile_info, name='profile'),
    url('search/', views.search, name='search'),
    url('update/',views.profile_update, name='update'),
    url('post_edit/', views.post_edit, name = 'post_edit'),
    url('api/merch/', views.MerchList.as_view()),
    url('api/merch/merch-id/(?P<pk>[0-9]+)/', views.MerchDescription.as_view())
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
