# Generated by Django 3.0.7 on 2020-07-02 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blogs', '0019_auto_20200702_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='my_blogs/static/blogimages/'),
        ),
    ]
