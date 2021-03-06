# Generated by Django 3.0.3 on 2020-02-05 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200204_2326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterModelOptions(
            name='detail',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='detail',
            name='date',
            field=models.DateField(verbose_name='Release Date'),
        ),
    ]
