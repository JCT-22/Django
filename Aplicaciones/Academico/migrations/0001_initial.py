# Generated by Django 3.0.14 on 2023-06-21 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=38)),
                ('creditos', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
