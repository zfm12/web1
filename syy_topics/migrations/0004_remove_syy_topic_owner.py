# Generated by Django 2.2.2 on 2019-06-11 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('syy_topics', '0003_auto_20190611_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='syy_topic',
            name='owner',
        ),
    ]
