# Generated by Django 4.2.4 on 2023-09-27 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontendvideos', '0007_alter_bootstraptutorial_tutorialtime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bootstraptutorial',
            name='tutorialTime',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='csstutorial',
            name='tutorialTime',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='htmltutorial',
            name='tutorialTime',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='javascripttutorial',
            name='tutorialTime',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reacttutorial',
            name='tutorialTime',
            field=models.IntegerField(default=0),
        ),
    ]
