# Generated by Django 4.2 on 2023-04-11 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModerationRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('flagged', models.BooleanField(default=False)),
                ('categories', models.JSONField()),
                ('category_scores', models.JSONField()),
            ],
        ),
    ]
