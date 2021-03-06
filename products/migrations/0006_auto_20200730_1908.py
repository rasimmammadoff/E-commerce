# Generated by Django 3.0.5 on 2020-07-30 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200725_1506'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Products'},
        ),
        migrations.AddField(
            model_name='category',
            name='gender',
            field=models.CharField(blank=True, choices=[('Men', 'Men'), ('Woman', 'Woman')], max_length=20, null=True),
        ),
    ]
