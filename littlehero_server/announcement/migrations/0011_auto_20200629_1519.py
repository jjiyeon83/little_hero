# Generated by Django 3.0.7 on 2020-06-29 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0010_auto_20200629_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='recruit_member',
            field=models.CharField(default='0 명 / 일', max_length=200),
        ),
    ]