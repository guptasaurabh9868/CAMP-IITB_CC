from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django_auth_ldap.backend import LDAPBackend


class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)
    # Other fields here
    uid = models.CharField(max_length=254)
    cn = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    first_name = models.CharField(max_length=254)
    uidChanged = models.BooleanField(default=False)
    # userPassword = models.CharField(max_length=254)
    # shadowLastChange = models.IntegerField(null=True)
    shadowexpire = models.CharField(null=False,max_length=20)
    # shadowWarning = models.IntegerField(null=True)
    # loginShell = models.CharField(max_length=254)
    roll_number = models.CharField(max_length=20)
    # gidNumber = models.IntegerField(null=True)
    # homeDirectory = models.CharField(max_length=254)
    # gecos = models.CharField(max_length=254)
    policy = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    # forwardedmail = models.CharField(max_length=254,default="khanepeena")
    accounttype = models.CharField(max_length=254)
    # l = models.CharField(max_length=254)
    telephoneNumber = models.CharField(max_length=254)

    def __str__(self):
        return self.user.username
    


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        new_profile = UserProfile.objects.create(user=instance)
        user = LDAPBackend().populate_user(instance.username)
        if user:
            roll_number = user.ldap_user.attrs.get("employeeNumber", [])[0]
            new_profile.roll_number = roll_number

            if user.ldap_user.attrs.get("uid", []) != []:
                uid = user.ldap_user.attrs.get("uid", [])[0]
                new_profile.uid = uid

            email = user.ldap_user.attrs.get("Email", [])[0]
            new_profile.Email = email

            first_name = user.ldap_user.attrs.get("first_name", [])[0]
            new_profile.first_name = first_name

            last_name = user.ldap_user.attrs.get("last_name", [])[0]
            new_profile.last_name = last_name

            new_profile.uidChanged = True

            cn = user.ldap_user.attrs.get("cn", [])[0]
            new_profile.cn = cn

            accounttype = user.ldap_user.attrs.get("employeetype", [])[0]
            new_profile.accounttype = accounttype
            
            # print(type(new_profile))
            shadowexpire = user.ldap_user.attrs.get('shadowexpire',[])[0]
            new_profile.shadowexpire = shadowexpire
            # print(type(shadowexpire))

            policy = user.ldap_user.attrs.get("policy", [])[0]
            new_profile.policy = policy

            new_profile.save()

post_save.connect(create_user_profile, sender=User)
