from django.db import models

# Create your models here.


class Display(models.Model):
    pre = models.CharField(max_length=200)
    major = models.CharField(max_length=500)
    post = models.CharField(max_length=500)

    def __str__(self):
        return self.major
