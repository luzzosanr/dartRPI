# Generated by Django 4.1.3 on 2022-12-02 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='time')),
                ('nb_players', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='ShotType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('multiplier', models.IntegerField(default=1)),
                ('gpio_pins', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Shot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.IntegerField(default=1)),
                ('game', models.ForeignKey(on_delete=models.SET(0), to='memory.game')),
                ('shot_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memory.shottype')),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_type', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=500)),
                ('game_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memory.gametype')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='game_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memory.gametype'),
        ),
    ]
