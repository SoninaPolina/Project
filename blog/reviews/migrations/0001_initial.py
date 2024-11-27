# Generated by Django 5.1.3 on 2024-11-27 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
                ('verification', models.BooleanField(default=False)),
            ],
        ),
    ]