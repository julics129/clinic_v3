# Generated by Django 3.1.4 on 2021-05-13 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc_v3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DummyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Print Prescription',
            },
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='doc_id',
        ),
    ]
