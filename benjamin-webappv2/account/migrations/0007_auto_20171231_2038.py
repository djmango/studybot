# Generated by Django 2.0 on 2018-01-01 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_guilds'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='settings',
            field=models.CharField(default='null', max_length=5000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='guilds',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='guilds',
            name='settings',
            field=models.CharField(max_length=5000),
        ),
    ]
