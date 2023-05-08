from django.db import models

# Create your models here.

class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=30)
    teacher_id = models.IntegerField()
    student_id = models.IntegerField()
    sendtype = models.CharField(max_length=30)
    rectype = models.CharField(max_length=30)
    # status = models.CharField(max_length=50)


    class Meta:
        managed = False
        db_table = 'chat'









