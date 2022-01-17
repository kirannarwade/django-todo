# Generated by Django 3.2.8 on 2022-01-14 13:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('1', '1️⃣'), ('2', '2️⃣'), ('3', '3️⃣'), ('4', '4️⃣'), ('5', '5️⃣'), ('6', '6️⃣'), ('7', '7️⃣'), ('8', '8️⃣'), ('9', '9️⃣'), ('10', '🔟')], default=datetime.datetime(2022, 1, 14, 13, 14, 11, 613075, tzinfo=utc), max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('C', 'COMPLETED'), ('P', 'PENDING')], default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
