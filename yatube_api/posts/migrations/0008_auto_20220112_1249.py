# Generated by Django 2.2.16 on 2022-01-12 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20220112_1057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follow',
            options={'ordering': ('user', 'following')},
        ),
    ]