# Generated by Django 5.0.3 on 2024-03-30 05:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='category_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='LittleLemonAPI.category'),
        ),
    ]
