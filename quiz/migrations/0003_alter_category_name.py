# Generated by Django 4.0.5 on 2022-06-30 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_alter_answers_options_alter_questions_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Frontend', 'Frontend'), ('Backend', 'Backend'), ('AWS', 'Aws-Devops'), ('Data_Science', 'Data Science'), ('Mobile', 'Mobile')], default='Backend', max_length=20),
        ),
    ]
