from django.db import models

# Create your models here.
class Members(models.Model):
    uname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    passwd = models.CharField(max_length=8)
    age = models.IntegerField()

    def __str__(self):
        return self.uname