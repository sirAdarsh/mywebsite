# Generated by Django 3.2.3 on 2021-07-20 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_alter_blogmodel_date_pub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='date_pub',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
