# Generated by Django 3.2.4 on 2021-07-03 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210627_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuser',
            name='user_id',
            field=models.BigIntegerField(unique=True, verbose_name='User telegram id'),
        ),
    ]
