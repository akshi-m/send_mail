# Generated by Django 4.1 on 2022-08-17 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promomail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='m_id',
            field=models.CharField(default='mail1', max_length=20, primary_key=True, serialize=False),
        ),
    ]
