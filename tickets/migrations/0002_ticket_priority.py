# Generated by Django 3.0.7 on 2020-07-06 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='priority',
            field=models.CharField(max_length=20, null=True),
        ),
    ]