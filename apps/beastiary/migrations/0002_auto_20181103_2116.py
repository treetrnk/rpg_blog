# Generated by Django 2.0.1 on 2018-11-04 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beastiary', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='npc',
            options={'ordering': ['title']},
        ),
        migrations.RemoveField(
            model_name='npc',
            name='banner',
        ),
        migrations.RemoveField(
            model_name='npc',
            name='body',
        ),
        migrations.RemoveField(
            model_name='npc',
            name='published_date',
        ),
        migrations.AddField(
            model_name='npc',
            name='aspects',
            field=models.TextField(blank=True, max_length=20000, null=True),
        ),
        migrations.AddField(
            model_name='npc',
            name='attributes',
            field=models.TextField(blank=True, max_length=20000, null=True),
        ),
        migrations.AddField(
            model_name='npc',
            name='description',
            field=models.TextField(blank=True, max_length=20000, null=True),
        ),
        migrations.AddField(
            model_name='npc',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='npc',
            name='image_src',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='npc',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='npc',
            name='stunts',
            field=models.TextField(blank=True, max_length=20000, null=True),
        ),
        migrations.AddField(
            model_name='npc',
            name='uses',
            field=models.TextField(blank=True, max_length=20000, null=True),
        ),
    ]