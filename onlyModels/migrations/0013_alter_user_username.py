# Generated by Django 4.0.6 on 2022-07-18 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlyModels', '0012_alter_profile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Username'),
        ),
    ]