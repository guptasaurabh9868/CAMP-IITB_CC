from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
               url(r'^depart_sysad/', views.depart_sysad, name='depart_sysad'),
               url(r'^changeuid/', views.changeuid, name='changeuid'),
               url(r'^hostel_sysad/', views.hostel_sysad, name='hostel_sysad'),
               url(r'^passwordchange/', views.passwordchange, name='passwordchange'),
               url(r'^modify_details/', views.modify_details, name='modify_details'),
               url(r'^setup_auto/', views.setup_auto, name='setup_auto'),
               url(r'^web_quota/', views.web_quota, name='web_quota'),
               url(r'^userinfo/', views.userinfo, name='userinfo'),
               url(r'', views.home, name='home'),

               # url(r'^logout/',views.home,name='home'),
               ]
