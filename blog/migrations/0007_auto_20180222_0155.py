# Generated by Django 2.0.2 on 2018-02-21 20:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_auto_20180221_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('subject', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Readarticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
                ('written_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r_subject', to='blog.Article')),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r_title', to='blog.Article')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r_updated_by', to=settings.AUTH_USER_MODEL)),
                ('written_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r_commented_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='publishtutorial',
            name='user',
        ),
        migrations.AlterField(
            model_name='author',
            name='about_author',
            field=models.TextField(max_length=4000, null=True),
        ),
        migrations.AlterField(
            model_name='commentblog',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic', to='blog.Article'),
        ),
        migrations.DeleteModel(
            name='PublishTutorial',
        ),
    ]
