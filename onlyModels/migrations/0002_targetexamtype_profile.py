# Generated by Django 4.0.6 on 2022-07-15 05:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlyModels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TargetExamType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Target Exam',
                'verbose_name_plural': 'Target Exams',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=150)),
                ('lname', models.CharField(max_length=150)),
                ('dob', models.DateField()),
                ('mobile', models.CharField(max_length=13)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('educational_details', models.JSONField(verbose_name='Educational Details')),
                ('role', models.IntegerField(choices=[('0', 'Student'), ('1', 'Examiner'), ('2', 'Both')], verbose_name='Selected Role')),
                ('target_exams', models.ManyToManyField(to='onlyModels.targetexamtype', verbose_name='Target Exam')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
