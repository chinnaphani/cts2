# Generated by Django 3.0.7 on 2020-07-06 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_ticket_ticketstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='tktdescription',
            field=models.TextField(null=True),
        ),
    ]
