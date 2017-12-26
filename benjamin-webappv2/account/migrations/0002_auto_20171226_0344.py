# Generated by Django 2.0 on 2017-12-26 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='avatar',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='guilds',
            field=models.CharField(default='null', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='token',
            field=models.CharField(default='null', max_length=50),
            preserve_default=False,
        ),
    ]