from django.db import models
from department.models import Department

# Create your models here.
class InternalExam(models.Model):
    exam_id = models.AutoField(db_column='Exam_id', primary_key=True)  # Field name made lowercase.
    # department_id = models.IntegerField('dept_id')
    department=models.ForeignKey(Department,to_field='department_id',on_delete=models.CASCADE)
    exam_subject = models.CharField(max_length=20)
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    time = models.TimeField(db_column='Time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'internal_exam'


