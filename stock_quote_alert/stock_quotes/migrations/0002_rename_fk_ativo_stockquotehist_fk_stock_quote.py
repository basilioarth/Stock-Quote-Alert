# Generated by Django 3.2.6 on 2021-11-11 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_quotes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockquotehist',
            old_name='fk_ativo',
            new_name='fk_stock_quote',
        ),
    ]
