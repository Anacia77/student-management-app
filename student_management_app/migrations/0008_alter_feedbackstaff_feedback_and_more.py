# Generated by Django 4.1.3 on 2023-01-24 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0007_alter_leavereportstaff_leave_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackstaff',
            name='feedback',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='feedbackstudent',
            name='feedback',
            field=models.TextField(),
        ),
    ]
