# Generated by Django 2.2.4 on 2019-09-11 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_text', models.CharField(max_length=400)),
                ('user_id', models.CharField(max_length=60)),
                ('tweet_id', models.CharField(max_length=100, unique=True)),
                ('date', models.DateField()),
                ('sentiment', models.FloatField()),
                ('likes', models.PositiveIntegerField()),
                ('retweets', models.PositiveIntegerField()),
                ('hashtags', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]
