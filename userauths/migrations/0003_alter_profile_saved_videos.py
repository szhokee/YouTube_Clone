# Generated by Django 3.2.7 on 2022-09-22 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_video_featured'),
        ('userauths', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='saved_videos',
            field=models.ManyToManyField(blank=True, null=True, related_name='saved_videos', to='core.Video'),
        ),
    ]
