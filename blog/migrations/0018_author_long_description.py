# Generated by Django 2.0.2 on 2018-02-23 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_author_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='long_description',
            field=models.TextField(max_length=10000, null=True),
        ),
    ]
