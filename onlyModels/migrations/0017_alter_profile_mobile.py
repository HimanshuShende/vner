# Generated by Django 4.0.6 on 2022-07-28 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlyModels', '0016_exam_rename_subjext_tags_question_subject_tags_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(max_length=20, verbose_name='Mobile'),
        ),
    ]
