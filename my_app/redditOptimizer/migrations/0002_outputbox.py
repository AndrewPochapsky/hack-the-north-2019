# Generated by Django 2.2.5 on 2019-09-14 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redditOptimizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutputBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subreddit1', models.CharField(max_length=100)),
                ('subreddit2', models.CharField(max_length=100)),
                ('subreddit3', models.CharField(max_length=100)),
                ('subreddit4', models.CharField(max_length=100)),
                ('subreddit5', models.CharField(max_length=100)),
            ],
        ),
    ]
