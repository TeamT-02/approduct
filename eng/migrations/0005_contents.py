# Generated by Django 4.2.4 on 2023-08-12 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eng', '0004_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
    ]
