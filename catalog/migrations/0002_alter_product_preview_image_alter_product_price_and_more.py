# Generated by Django 4.2.3 on 2023-07-26 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='preview_image',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='specification',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]