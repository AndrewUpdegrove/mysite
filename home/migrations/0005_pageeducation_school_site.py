# Generated by Django 3.0.8 on 2020-10-22 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20201022_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageeducation',
            name='school_site',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
