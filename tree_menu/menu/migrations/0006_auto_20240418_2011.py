# Generated by Django 2.2.19 on 2024-04-18 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20240418_2011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ('id',), 'verbose_name': 'Меню', 'verbose_name_plural': 'Меню'},
        ),
    ]