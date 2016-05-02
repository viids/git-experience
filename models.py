from django.db import models

# Create your models here.


class SignUp(models.Model):
    email = models.EmailField()
    fullName = models.CharField(max_length=120, blank=True, null=True)
    timeStamp = models. DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):  # python2 __unicode__
        return self.email

    # class Meta:
    #     ordering = ["name"]


class Newspapers(models.Model):
    name = models.CharField(max_length= 120, blank=False, null=False)
    pub_date = models.DateField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name

