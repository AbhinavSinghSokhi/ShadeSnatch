# Generated by Django 5.0.6 on 2024-06-10 12:32

import shade_Snatch_App.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shade_Snatch_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=shade_Snatch_App.models.custom_upload_path),
        ),
    ]
