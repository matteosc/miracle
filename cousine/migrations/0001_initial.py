# Generated by Django 4.2.4 on 2023-09-09 11:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personnel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cousine.category')),
            ],
        ),
        migrations.CreateModel(
            name='Nutritionals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories', models.FloatField()),
                ('carbohydrates', models.FloatField()),
                ('proteins', models.FloatField()),
                ('fat', models.FloatField()),
                ('starch', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='OrdineCucina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('status', models.CharField(max_length=20)),
                ('note', models.TextField(null=True)),
                ('richiedente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='personnel.personnel')),
            ],
        ),
        migrations.CreateModel(
            name='VociOrdineCucina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('um', models.CharField(max_length=20)),
                ('quantity', models.FloatField()),
                ('note', models.TextField()),
                ('ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cousine.ingredient')),
                ('ordine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cousine.ordinecucina')),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='nutritional',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cousine.nutritionals'),
        ),
    ]
