# Generated by Django 4.2.6 on 2023-10-20 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lhs', models.IntegerField()),
                ('rhs', models.IntegerField()),
                ('result', models.IntegerField()),
                ('operator', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Divide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lhs', models.IntegerField()),
                ('rhs', models.IntegerField()),
                ('result', models.IntegerField()),
                ('operator', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Multiply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lhs', models.IntegerField()),
                ('rhs', models.IntegerField()),
                ('result', models.IntegerField()),
                ('operator', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Subtract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lhs', models.IntegerField()),
                ('rhs', models.IntegerField()),
                ('result', models.IntegerField()),
                ('operator', models.CharField(max_length=1)),
            ],
        ),
    ]
