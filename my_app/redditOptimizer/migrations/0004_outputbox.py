# Generated by Django 2.2.5 on 2019-09-15 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redditOptimizer', '0003_delete_outputbox'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutputBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subred', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
    ]
