# Generated by Django 2.2.4 on 2019-10-22 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Twitter', '0002_remove_tweet_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wordlist',
            options={'ordering': ('word',)},
        ),
    ]
