from django.db import models

# Create your models here.
class StudyMaterials(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=20)
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    time = models.TimeField(db_column='Time')  # Field name made lowercase.
    study_material = models.CharField(db_column='Study_material', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'study_materials'
