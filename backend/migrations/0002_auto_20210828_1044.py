# Generated by Django 3.2.6 on 2021-08-28 14:44

import backend.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('contact_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('business_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=30)),
                ('zip', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.contacts')),
            ],
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('request_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('request_text', models.CharField(max_length=500)),
                ('post_date', models.DateTimeField(verbose_name='date posted')),
                ('request_photo', models.ImageField(upload_to=backend.models.request_directory_path)),
                ('contact_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.contacts')),
            ],
        ),
        migrations.DeleteModel(
            name='Request',
        ),
        migrations.AddField(
            model_name='order',
            name='request_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.requests'),
        ),
    ]
