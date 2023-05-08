from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    roll_no = models.IntegerField()
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    phone = models.IntegerField()
    department = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'student'

