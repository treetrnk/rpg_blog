# Generated by Django 2.0.1 on 2018-11-10 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beastiary', '0004_auto_20181110_0633'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consequence',
            options={'ordering': ['slots']},
        ),
        migrations.AlterModelOptions(
            name='stress',
            options={'ordering': ['boxes']},
        ),
    ]
