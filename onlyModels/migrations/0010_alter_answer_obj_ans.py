# Generated by Django 4.0.6 on 2022-07-18 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlyModels', '0009_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='obj_ans',
            field=models.ManyToManyField(blank=True, to='onlyModels.option', verbose_name='Objective Answer'),
        ),
    ]
