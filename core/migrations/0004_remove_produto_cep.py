# Generated by Django 4.0 on 2021-12-27 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_categoria_criado_por'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='cep',
        ),
    ]
