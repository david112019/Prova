# Generated by Django 2.1.7 on 2019-04-01 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.TextField()),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=30)),
            ],
        ),
    ]
