# Generated by Django 2.2.2 on 2019-06-11 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('syy_topics', '0002_auto_20190611_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syy_topic',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]