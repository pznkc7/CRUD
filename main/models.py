from django.db import models

# Create your models here.

# var1 = (('M','Medical_reason'),('P','Personal_reason'),('E','Emergency_reason'))
class StudentLeave(models.Model):
   roll_number =models.CharField(max_length=6,unique=True)
   full_name =models.CharField(max_length=100)
   faculty =models.CharField(max_length=100)
   semester =models.PositiveIntegerField()
   start_date =models.DateField()
   end_date =models.DateField()
   leave_type =models.CharField(max_length=100)
   reason =models.TextField()
   guardian_contact =models.CharField(max_length=13)
   is_delete = models.BooleanField(default=False)
   delete_time = models.DateTimeField(null=True)
   student_email = models.EmailField(max_length=100)

    