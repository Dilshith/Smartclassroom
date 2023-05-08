from django.db import models
from department.models import Department
# Create your models here.
class TimeTable(models.Model):
    table_id = models.AutoField(primary_key=True)
    # department_id = models.IntegerField()
    department=models.ForeignKey(Department,to_field='department_id',on_delete=models.CASCADE)
    time_table = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'time_table'
