# Generated by Django 3.1.5 on 2021-01-24 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wardapp', '0005_auto_20210124_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='AwardMerch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('design', models.TextField()),
                ('usability', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
    ]
