# Generated by Django 2.2.2 on 2019-06-24 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollNo', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('mark', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
    ]
