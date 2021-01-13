from django.contrib import admin
from django.conf.urls import include, url
from libs.views import *

urlpatterns = [
    url(r'^logout/$', Logout, name='logout'),
    url(r'^register-member/$', register, name='register-member'),
    url(r'^user-profile/$', user_profile, name='user-profile'),
    url(r'^update-confirmation/$', update_confirmation, name='update-confirmation'),
    url(r'^add-dict/$', add_dict, name='add-dict'),
    url(r'^', dashboard, name='dashboard'),



]