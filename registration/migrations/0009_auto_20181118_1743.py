# Generated by Django 2.1.2 on 2018-11-18 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_auto_20181117_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Neutral', 'Neutral')], default='Neutral', max_length=10),
        ),
    ]
