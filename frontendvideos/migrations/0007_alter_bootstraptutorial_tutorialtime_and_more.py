# Generated by Django 4.2.4 on 2023-09-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontendvideos', '0006_bootstraptutorial_tutorialtime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bootstraptutorial',
            name='tutorialTime',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='csstutorial',
            name='tutorialTime',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='htmltutorial',
            name='tutorialTime',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='javascripttutorial',
            name='tutorialTime',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='reacttutorial',
            name='tutorialTime',
            field=models.CharField(max_length=20),
        ),
    ]
