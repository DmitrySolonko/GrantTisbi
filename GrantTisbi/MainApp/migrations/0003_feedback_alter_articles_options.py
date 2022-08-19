# Generated by Django 4.0.6 on 2022-08-07 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_alter_articles_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=100, verbose_name='ФИО')),
                ('email', models.CharField(max_length=150, verbose_name='Почтовый адрес')),
                ('text', models.TextField(verbose_name='Сообщение')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')),
            ],
            options={
                'verbose_name': 'заявка из обратной связи',
                'verbose_name_plural': 'заявки из обратной связи',
                'ordering': ['date'],
            },
        ),
        migrations.AlterModelOptions(
            name='articles',
            options={'ordering': ['created_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]
