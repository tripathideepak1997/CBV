# Generated by Django 2.1.7 on 2019-03-28 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='school', to='app1.School'),
        ),
    ]
