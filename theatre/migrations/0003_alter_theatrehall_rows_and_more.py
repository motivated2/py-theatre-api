# Generated by Django 5.0.3 on 2024-03-27 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theatrehall',
            name='rows',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='theatrehall',
            name='seats_in_row',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='row',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='seat',
            field=models.PositiveIntegerField(),
        ),
    ]
