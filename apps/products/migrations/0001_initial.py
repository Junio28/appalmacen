# Generated by Django 3.0.5 on 2020-04-10 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('quantity', models.IntegerField(verbose_name='Cantidad')),
                ('price', models.IntegerField(verbose_name='Precio')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('mark', models.CharField(max_length=50, verbose_name='Marca')),
                ('product_types', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ProductType')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': ' productos',
            },
        ),
    ]
