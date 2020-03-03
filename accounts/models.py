from django.db import models

# Create your models here.
class SMS_veri(models.Model):
    mobile_number = models.CharField(max_length=15)
    otp = models.CharField(max_length=7)
    tran_id = models.CharField(max_length=30)
    verified = models.BooleanField()
    date = models.DateField()

class Meta:
    db_table = 'SMS_veri'