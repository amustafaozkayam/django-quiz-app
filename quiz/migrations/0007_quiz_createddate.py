# Generated by Django 4.0.5 on 2022-06-30 21:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='createdDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
