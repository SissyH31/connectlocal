# Generated by Django 3.2.6 on 2021-08-28 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20210828_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='business_type',
            field=models.CharField(choices=[('R', 'Restaurant'), ('F', 'Farm')], default='R', max_length=1),
        ),
        migrations.AddField(
            model_name='requests',
            name='fullfilled',
            field=models.BooleanField(default=False),
        ),
    ]
