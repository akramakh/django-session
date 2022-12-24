# Generated by Django 2.2.28 on 2022-12-24 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('num_of_pages', models.IntegerField(default=1)),
                ('content', models.TextField()),
            ],
        ),
    ]
