# Generated by Django 3.2.5 on 2021-08-10 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0004_auto_20210810_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=24)),
            ],
        ),
        migrations.AddField(
            model_name='action',
            name='tag',
            field=models.ManyToManyField(to='resume_app.TagJob'),
        ),
    ]
