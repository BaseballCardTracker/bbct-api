# Generated by Django 3.1.7 on 2021-03-14 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseballCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autographed', models.BooleanField(default=False)),
                ('condition', models.CharField(max_length=32)),
                ('brand', models.CharField(max_length=32)),
                ('year', models.IntegerField()),
                ('number', models.CharField(max_length=32)),
                ('value', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('quantity', models.IntegerField()),
                ('player', models.CharField(max_length=32)),
                ('team', models.CharField(max_length=32)),
                ('position', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cards', models.ManyToManyField(to='api.BaseballCard')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
