# Generated by Django 2.2.2 on 2019-06-12 12:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('syy_topics', '0006_auto_20190611_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='syy_entry',
            options={'verbose_name_plural': 'entries'},
        ),
        migrations.AlterModelOptions(
            name='syy_topic',
            options={},
        ),
        migrations.AlterField(
            model_name='syy_entry',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='文章标题'),
        ),
    ]
