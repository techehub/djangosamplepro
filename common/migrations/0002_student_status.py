# Generated by Django 2.2.2 on 2019-06-24 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(default='P', max_length=1),
        ),
    ]