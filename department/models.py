from django.db import models

# Create your models here.
class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(db_column='Department_name', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'department'
