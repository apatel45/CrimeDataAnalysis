# Generated by Django 4.2.4 on 2024-04-11 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0005_alter_news_img1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='Media/'),
        ),
    ]
