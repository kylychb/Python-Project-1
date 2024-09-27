# Generated by Django 5.1.1 on 2024-09-20 07:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='item', verbose_name='Изображение товара')),
                ('price', models.CharField(max_length=20, verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание')),
                ('is_like', models.BooleanField(default=False, verbose_name='Нравится')),
                ('created_at', models.DateTimeField(verbose_name='Время создания')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='item', to='cards.category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['created_at'],
            },
        ),
    ]
