# Generated by Django 4.2.4 on 2024-04-11 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=2000)),
                ('author', models.CharField(max_length=100)),
                ('pubdate', models.DateField()),
                ('category', models.CharField(max_length=50)),
                ('source', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
    ]