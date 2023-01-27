# Generated by Django 4.1.3 on 2023-01-24 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0005_alter_sessionyearmodel_managers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendancereport',
            name='course_id',
        ),
        migrations.AddField(
            model_name='attendancereport',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='attendancereport',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]