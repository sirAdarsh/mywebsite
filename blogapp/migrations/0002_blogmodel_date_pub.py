# Generated by Django 3.2.3 on 2021-07-20 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='date_pub',
            field=models.CharField(default='', max_length=15),
        ),
    ]
