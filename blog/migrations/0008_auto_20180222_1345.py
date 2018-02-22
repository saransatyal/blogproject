# Generated by Django 2.0.2 on 2018-02-22 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180222_0155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readarticle',
            name='subject',
        ),
        migrations.AddField(
            model_name='article',
            name='document',
            field=models.FileField(default=2, upload_to='documents/'),
            preserve_default=False,
        ),
    ]
