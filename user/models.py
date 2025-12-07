from django.db import models

# Create your models here.
class Userlist(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    age = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userlist'