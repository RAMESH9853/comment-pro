# Generated by Django 4.1.3 on 2022-12-20 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentdata',
            name='comment',
            field=models.CharField(max_length=500),
        ),
    ]
