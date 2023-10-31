from django.contrib import admin
from django.db import models
from django.contrib.admin import AdminSite
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse
# Register your models here.

class CustomAdminSite(AdminSite):
    def index(self, request, extra_context=None):
        if request.user.is_authenticated:
            return redirect('/admin/addcameraLocation/')
        else:
            return super().index(request, extra_context)
admin_site = CustomAdminSite(name='custom_admin')
admin.site = admin_site 
admin.autodiscover()
def __str__(self):
        return self.name
