# Generated by Django 4.1.2 on 2022-10-28 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_song_artiste'),
    ]

    operations = [
        migrations.AddField(
            model_name='lyric',
            name='Song',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='musicapp.song'),
            preserve_default=False,
        ),
    ]
