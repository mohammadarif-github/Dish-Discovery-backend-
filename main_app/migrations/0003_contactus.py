# Generated by Django 5.0.1 on 2024-04-29 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_recipemodel_ingredients'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('problem', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contact Us',
            },
        ),
    ]
