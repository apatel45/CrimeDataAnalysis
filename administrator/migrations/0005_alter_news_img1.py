# Generated by Django 4.2.4 on 2024-04-11 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0004_news_img1_news_img2_news_img3_news_img4_news_img5'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='media/Media/'),
        ),
    ]
