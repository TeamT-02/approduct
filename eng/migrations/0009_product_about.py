# Generated by Django 4.2.4 on 2023-08-12 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eng', '0008_product_alter_about_images_alter_motto_images_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]