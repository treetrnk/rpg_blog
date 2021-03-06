# Generated by Django 2.0.1 on 2018-10-11 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20180124_0154'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='height',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='width',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(height_field='height', upload_to='', width_field='width'),
        ),
    ]
