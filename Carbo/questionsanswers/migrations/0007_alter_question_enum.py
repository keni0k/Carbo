# Generated by Django 3.2.8 on 2021-11-23 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionsanswers', '0006_auto_20211123_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='enum',
            field=models.CharField(max_length=255, unique=True, verbose_name='Unique str identifier'),
        ),
    ]
