# Generated by Django 5.0.3 on 2024-03-26 19:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookListDRF', '0002_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='BookListDRF.genre'),
        ),
    ]