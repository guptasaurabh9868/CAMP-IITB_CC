from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import ldap
from django_auth_ldap.config import LDAPSearch
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django_auth_ldap.backend import _LDAPUser, LDAPBackend
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
import datetime
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
# from django.core.mixins import SensitivePostParametersMixin

# from .forms import LoginForm

# Create your views here.

# class LoginView(View):
#     """
#     GET: If user is already logged in then redirect to 'next' parameter in query_params
#         Else render the login form
#     POST:
#         Validate form, login user
#     """
#     form_class = LoginForm
#     template_name = 'home/main.html'


def home(request):
    login_failed = False
    authorized_Access = True
    if request.POST:
        # form = self.form_class(request.POST)
        # next_ = request.POST.get('next', settings.LOGIN_REDIRECT_URL)
        # if next_ == '':
        #     next_ = settings.LOGIN_REDIRECT_URL
        usern = request.POST.get("username", '')
        passw = request.POST.get("password", '')
        # if form.is_valid():
        #     username = form.cleaned_data['username']
        #     password = form.cleaned_data['password']
        # remember = form.cleaned_data['remember']

        user = authenticate(username=usern, password=passw)
        if user is not None:
                # if remember:
                #     # Yearlong Session
                #     request.session.set_expiry(24 * 365 * 3600)
                # else:
                #     request.session.set_expiry(0)
            # request.Session.set_expiry(30 * 60)
            login(request, user)
            # ldapuserprofile = UserProfile.objects.get_or_create(username=user.username)
            # context = {'request': request, 'ldapuser': ldapuserprofile,}
            # return render(request, 'home/userinfo.html')
            return redirect('/userinfo/')
        else:
            login_failed = True
            # return render(request, 'home/after_login.html')
                # form.add_error(None, "Unable to authorize user. Try again!")
    return render(request, 'home/main.html', {'login_failed': login_failed,'authorized_Access':authorized_Access})


def userinfo(request):
    if request.POST:
        logout(request)
        # return render(request, 'home/main.html')
        return HttpResponseRedirect('/')
    else:
        # print(request.user.userprofile.uid)
        # print(request.user.userprofile.cn)
        # print(request.user.email)
        # print(request.user.first_name)
        # print(request.user.last_name)
        # print(request.user.userprofile.uidChanged)
        # print(request.user.userprofile.userPassword)
        # print(request.user.userprofile.shadowexpire)
        # print(request.user.userprofile.roll_number)
        # print(request.user.userprofile.policy)
        # print(request.user.userprofile.accounttype)
        # try:
        #     ldapuserprofile = UserProfile.objects.get(uid=request.user.username)
        # except UserProfile.DoesNotExist:
        #     LDAPBackend().populate_user(request.user.username)
        #     context = {'request': request, 'ldapuser': ldapuserprofile,}
        #     return render(request, 'home/userinfo.html',context)
        #     # return HttpResponseRedirect('/logout/')
        # context = {'request': request, 'ldapuser': ldapuserprofile,}
        if request.user.is_authenticated:
            start_date = "01-01-1970"
            date_1 = datetime.datetime.strptime(start_date, "%m-%d-%Y")
            end_date = date_1 + datetime.timedelta(days=int(request.user.userprofile.shadowexpire.strip()))
            # print(end_date)
            # print(check_password("", request.user.password))
            # print(request.user.password)
            return render(request, 'home/userinfo.html',{'shadowexpire':end_date})
        else:
            return render(request, 'home/userinfo.html')


# @login_required
# def userinfo(request):
#     try:
#         ldapuserprofile = UserProfile.objects.get(username=request.user.username)
#     except UserProfile.DoesNotExist:
#         return HttpResponseRedirect('/logout/')
#     context = {'request': request, 'ldapuser': ldapuserprofile,}
#     return render(request, 'home/userinfo.html', context)

def depart_sysad(request):
    return render(request,'home/depart_sysad.html')
def changeuid(request):
    return render(request,'home/changeuid.html')
def hostel_sysad(request):
    return render(request,'home/hostel_sysad.html')
# def passwordchange(request):
#     if request.POST:
#         print("Hello")
#         passw = request.POST.get("new_password", '')
#         user = User.objects.get(request.user.username)
#         user.set_password(new_password)
#         return render(request,'home/passwordchange.html')
#     else:
#         return render(request,'home/passwordchange.html')
def passwordchange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('passwordchange')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'home/passwordchange.html', {'form': form})

def modify_details(request):
    return render(request,'home/modify-details.html')
def setup_auto(request):
    return render(request,'home/setup_auto.html')
def web_quota(request):
    return render(request,'home/web_quota.html')