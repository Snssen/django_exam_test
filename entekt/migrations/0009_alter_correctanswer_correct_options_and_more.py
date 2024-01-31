# Generated by Django 4.1.7 on 2024-01-06 17:48

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('entekt', '0008_alter_correctanswer_correct_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correctanswer',
            name='correct_options',
            field=models.ManyToManyField(blank=True, limit_choices_to={'quest_id': django.db.models.expressions.OuterRef('quest_id')}, null=True, related_name='correct_for_question', to='entekt.option'),
        ),
        migrations.AlterField(
            model_name='correctanswer',
            name='quest',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='correct_answers', to='entekt.quest'),
        ),
    ]
