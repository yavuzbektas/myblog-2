# Generated by Django 3.0.5 on 2020-04-02 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20200402_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='İçerik'),
        ),
    ]
