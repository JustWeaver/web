# Generated by Django 3.2.25 on 2025-03-12 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_itemvariationbonuses_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemvariation',
            name='market_type',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
