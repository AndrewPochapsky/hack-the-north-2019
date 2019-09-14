# Generated by Django 2.2.5 on 2019-09-14 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InputBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('return_number', models.PositiveSmallIntegerField(verbose_name='Return Number')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField(blank=True)),
            ],
        ),
    ]
