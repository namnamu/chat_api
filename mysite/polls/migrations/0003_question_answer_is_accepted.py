# Generated by Django 4.2.3 on 2023-11-07 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0002_question_answer_delete_choice_delete_question"),
    ]

    operations = [
        migrations.AddField(
            model_name="question_answer",
            name="is_accepted",
            field=models.BooleanField(default=False),
        ),
    ]
