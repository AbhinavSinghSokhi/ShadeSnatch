# Generated by Django 5.0.6 on 2024-06-10 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shade_Snatch_App', '0002_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
