# Generated by Django 3.2.9 on 2022-01-17 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend_work', '0003_commentsmodel_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentsmodel',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='backend_work.postmodel'),
        ),
    ]
