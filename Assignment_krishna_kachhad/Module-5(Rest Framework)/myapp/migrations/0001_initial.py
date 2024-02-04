# Generated by Django 4.2.6 on 2024-02-04 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('isbn', models.BigIntegerField()),
                ('publisher', models.CharField(max_length=20)),
            ],
        ),
    ]
