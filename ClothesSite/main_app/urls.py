from django.conf import settings
from django.conf.urls import url
from django.views.static import serve

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'post_url/', views.post_clothes_item, name='post_clothes_item'),
    url(r'([0-9]+)/$', views.detail, name='detail'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^favorite_clothes_item/$', views.favorite_clothes_item, name='favorite_clothes_item'),
    url(r'^unfavorite_clothes_item/$', views.unfavorite_clothes_item, name='unfavorite_clothes_item'),
    url(r'^feedback/$', views.feedback, name='feedback'),
]


#Helper method to serve media files locally
#Sends any url that matches /media to static.serve()
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,}),
    ]



