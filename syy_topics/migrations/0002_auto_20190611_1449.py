# Generated by Django 2.2.2 on 2019-06-11 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('syy_topics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syy_topic',
            name='owner',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='SYY_Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('owner', models.CharField(max_length=50)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syy_topics.SYY_Topic')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]