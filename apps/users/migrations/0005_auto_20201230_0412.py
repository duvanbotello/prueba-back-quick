# Generated by Django 3.1.4 on 2020-12-30 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201230_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='token',
            field=models.CharField(max_length=255, verbose_name='Token'),
        ),
    ]