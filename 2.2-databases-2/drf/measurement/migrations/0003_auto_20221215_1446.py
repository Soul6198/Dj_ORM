# Generated by Django 3.1.2 on 2022-12-15 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_auto_20221215_1445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='temperature',
            new_name='changing_temp',
        ),
    ]
