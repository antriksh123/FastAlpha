# Generated by Django 3.1.7 on 2021-02-28 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_company_header'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='header',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
