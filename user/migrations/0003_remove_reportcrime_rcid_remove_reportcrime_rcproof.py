# Generated by Django 4.2.4 on 2024-02-15 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_reportcrime_alter_register_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportcrime',
            name='rcid',
        ),
        migrations.RemoveField(
            model_name='reportcrime',
            name='rcproof',
        ),
    ]
