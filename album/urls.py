from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index, name = 'home'),
    url('^$',views.picture_of_day,name='pictureToday'),
]
