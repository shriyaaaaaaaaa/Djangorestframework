# Generated by Django 5.1.6 on 2025-02-18 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='roll',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
