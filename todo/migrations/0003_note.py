# Generated by Django 2.0.7 on 2018-07-28 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20180728_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=1024)),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Todo')),
            ],
        ),
    ]
