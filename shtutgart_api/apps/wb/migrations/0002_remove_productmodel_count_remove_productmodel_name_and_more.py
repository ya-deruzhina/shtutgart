# Generated by Django 4.1 on 2024-10-15 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='count',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='name',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='brand_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='color',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='contents',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='name_product',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='options',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='price_without_nds',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='root_type_product',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='type_product',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='vendor_code',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
