from django.db import models

# Create your models here.
class table(models.Model):
    name = models.CharField(default='',max_length=200)
    email = models.EmailField(default='',max_length=200)
    num = models.PositiveBigIntegerField(default=0)
    c_pass = models.CharField(default='', max_length=200)