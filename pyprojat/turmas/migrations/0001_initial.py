# Generated by Django 3.1.3 on 2020-11-12 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('nome', models.CharField(max_length=64)),
                ('slug', models.SlugField(unique=True)),
                ('inicio', models.DateTimeField()),
                ('fim', models.DateTimeField()),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
    ]
