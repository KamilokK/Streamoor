from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STREAM_TYPE = (
    (1, "Netflix"),
    (2, "HBO GO"),
    (3, "Amazon Prime"),
)


class StreamoorUser(models.Model):

    user_stream= models.IntegerField(choices=STREAM_TYPE)

    user = models.OneToOneField(User, on_delete=models.CASCADE)





class UsersConnection(models.Model):
    user_1 = models.ForeignKey(StreamoorUser, on_delete=models.CASCADE, related_name='pierwszy')
    user_2 = models.ForeignKey(StreamoorUser, on_delete=models.CASCADE, related_name='drugi')

