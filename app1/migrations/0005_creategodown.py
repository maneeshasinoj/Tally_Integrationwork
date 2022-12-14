# Generated by Django 4.0.5 on 2022-09-10 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_delete_creategodown'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateGodown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alias', models.CharField(max_length=100)),
                ('under_name', models.CharField(max_length=50)),
                ('comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.companies')),
            ],
        ),
    ]
