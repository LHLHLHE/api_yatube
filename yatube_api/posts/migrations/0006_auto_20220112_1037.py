# Generated by Django 2.2.16 on 2022-01-12 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20220110_1924'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterModelOptions(
            name='follow',
            options={'ordering': ('following',)},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ('title',)},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-pub_date',)},
        ),
    ]