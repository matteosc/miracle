# Generated by Django 4.2.4 on 2023-08-23 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cousine', '0002_nutritionals_ingredient_nutritional'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('unitaArrivo', models.IntegerField()),
                ('giacenza', models.FloatField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cousine.ingredient')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supply.supplier')),
            ],
        ),
    ]