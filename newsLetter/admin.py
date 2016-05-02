from django.contrib import admin
from django.db import models

# Register your models here.
from .forms import SignUpForm
from .models import SignUp
from .models import Newspapers


class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__str__", "timeStamp", "update"]
    form = SignUpForm

    # class Meta:
        # model = SignUp


class NewspaperAdmin(admin.ModelAdmin):
    list_display = ["__str__", "pub_date"]

    class Meta:
        model = Newspapers

admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Newspapers, NewspaperAdmin)
