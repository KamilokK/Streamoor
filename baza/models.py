from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STREAM_TYPE = (
    (1, "Netflix"),
    (2, "HboGo"),
    (3, "Amazon Prime"),
)


class StreamoorUser(models.Model):
    name = models.CharField(max_length=64, null=False)
    email = models.EmailField()
    user_stream= models.IntegerField(choices=STREAM_TYPE)
    password = models.CharField(max_length=32)
    create_date = models.DateTimeField(auto_now_add=True)

    user = models.OneToOneField(User)



class UsersStream(models.Model):
    user_stream = models.ForeignKey(StreamoorUser, on_delete=models.CASCADE)
    stream_type = models.IntegerField(choices=STREAM_TYPE, null=False)