# Generated by Django 2.1 on 2018-08-11 18:47

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20180811_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
