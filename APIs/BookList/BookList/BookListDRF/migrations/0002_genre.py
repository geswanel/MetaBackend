# Generated by Django 5.0.3 on 2024-03-26 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookListDRF', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(default='Fiction', max_length=255)),
            ],
        ),
    ]
