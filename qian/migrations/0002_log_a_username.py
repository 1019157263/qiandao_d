# Generated by Django 2.1.1 on 2018-09-11 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qian', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log_a',
            name='username',
            field=models.CharField(default='777', max_length=200),
            preserve_default=False,
        ),
    ]
