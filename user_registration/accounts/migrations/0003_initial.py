# Generated by Django 5.2 on 2025-04-09 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='DynamicRow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField(default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
