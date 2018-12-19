from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STREAM_TYPE = (
    (1, "Netflix"),
    (2, "HboGo"),
    (3, "Amazon Prime"),
)


class StreamoorUser(models.Model):

    user_stream= models.IntegerField(choices=STREAM_TYPE)

    user = models.OneToOneField(User, on_delete=models.CASCADE)



class UsersStream(models.Model):
    user_stream = models.ForeignKey(StreamoorUser, on_delete=models.CASCADE)
    stream_type = models.IntegerField(choices=STREAM_TYPE, null=False)