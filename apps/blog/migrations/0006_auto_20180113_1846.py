# Generated by Django 2.0.1 on 2018-01-13 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180113_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.FileField(upload_to='apps/blog/static/blog/images/'),
        ),
    ]
