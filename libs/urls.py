from django.contrib import admin
from django.conf.urls import include, url
from libs.views import *

urlpatterns = [

    url(r'^home/', index, name='home'),
    url(r'^add-ad/', add_ads, name='add-ad'),
    url(r'^ad-detail/(?P<id>.*)$', ad_detail, name='ad-detail'),
    url(r'^list-by-category/(?P<id>.*)$', category, name='list-by-category'),
    url(r'^master/', master, name='master'),
    url(r'^detail/', detail, name='detail'),

    url(r'^videos/', video, name='videos'),
    url(r'^issues/', issues, name='issues'),





]
