# Generated by Django 4.1.3 on 2022-11-05 11:57

from django.db import migrations, models
import my_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0005_page_delete_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='image',
            field=models.ImageField(upload_to=my_api.models.date_upload_to),
        ),
    ]