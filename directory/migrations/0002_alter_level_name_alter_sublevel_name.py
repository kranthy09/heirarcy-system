# Generated by Django 4.1.2 on 2022-10-14 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='sublevel',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]