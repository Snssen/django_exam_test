# Generated by Django 4.1.7 on 2024-01-06 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entekt', '0007_alter_correctanswer_correct_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correctanswer',
            name='correct_options',
            field=models.ManyToManyField(limit_choices_to={'quest_id': models.F('quest_id')}, to='entekt.option'),
        ),
    ]