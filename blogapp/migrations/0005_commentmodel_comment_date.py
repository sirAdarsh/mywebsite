# Generated by Django 3.2.3 on 2021-07-20 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_alter_blogmodel_date_pub'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='comment_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
