# Generated by Django 3.0.7 on 2020-06-19 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blogs', '0006_auto_20200618_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='dislikes',
            field=models.IntegerField(blank=True, default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='blog',
            name='likes',
            field=models.IntegerField(blank=True, default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='blog',
            name='user_id',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
