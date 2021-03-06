# Generated by Django 2.0.4 on 2018-04-27 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('saves', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('summa', models.DecimalField(decimal_places=2, max_digits=15)),
                ('notes', models.TextField(blank=True, null=True)),
                ('fsave', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='saves.Save')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sources.Source')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'incomes',
            },
        ),
    ]
