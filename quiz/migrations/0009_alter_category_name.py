# Generated by Django 4.0.5 on 2022-07-01 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_category_createddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Frontend', 'Frontend'), ('Backend', 'Backend'), ('Aws', 'Aws-Devops'), ('Data_Science', 'Data_Science'), ('Mobile', 'Mobile')], default='Backend', max_length=20),
        ),
    ]
