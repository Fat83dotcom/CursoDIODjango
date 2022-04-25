# Generated by Django 4.0.4 on 2022-04-25 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='usuario',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evento',
            name='dataCriacao',
            field=models.DateTimeField(auto_now=True, verbose_name='data da criação'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='dataEvento',
            field=models.DateTimeField(verbose_name='data do evento'),
        ),
    ]
