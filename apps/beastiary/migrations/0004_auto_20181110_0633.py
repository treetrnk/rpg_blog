# Generated by Django 2.0.1 on 2018-11-10 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beastiary', '0003_auto_20181110_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consequence',
            name='slots',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='stress',
            name='boxes',
            field=models.TextField(max_length=1000),
        ),
    ]
