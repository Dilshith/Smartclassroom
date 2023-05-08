from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    department = models.CharField(max_length=40)
    qualification = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'teacher'
