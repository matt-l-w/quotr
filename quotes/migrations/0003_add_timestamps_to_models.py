# Generated by Django 2.2.5 on 2019-10-01 12:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_quote_page_number_can_be_null'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='quote',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quote',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='page',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
