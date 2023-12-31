# Generated by Django 4.2.4 on 2023-08-12 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eng', '0005_contents'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='_storage/media/motto/en/')),
                ('name', models.CharField(max_length=250)),
                ('text', models.TextField()),
            ],
        ),
    ]
