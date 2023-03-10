# Generated by Django 4.1.3 on 2023-02-07 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0009_alter_attendance_attendance_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineClassRoom',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('room_name', models.CharField(max_length=255)),
                ('room_pwd', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('session_years', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.sessionyearmodel')),
                ('started_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.staff')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.subjects')),
            ],
        ),
    ]
