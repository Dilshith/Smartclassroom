# Generated by Django 3.2.4 on 2023-01-06 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InternalExam',
            fields=[
                ('exam_id', models.AutoField(db_column='Exam_id', primary_key=True, serialize=False)),
                ('department_id', models.IntegerField()),
                ('exam_subject', models.CharField(max_length=20)),
                ('date', models.DateField(db_column='Date')),
                ('time', models.TimeField(db_column='Time')),
            ],
            options={
                'db_table': 'internal_exam',
                'managed': False,
            },
        ),
    ]
