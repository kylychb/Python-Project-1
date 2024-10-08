# Generated by Django 5.1.1 on 2024-09-20 07:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_item'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категория'},
        ),
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
        migrations.AddField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.CreateModel(
            name='ItemImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='item', verbose_name='Изоброжение')),
                ('image_mobile', models.ImageField(upload_to='item', verbose_name='Изоброжение')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_images', to='cards.item')),
            ],
            options={
                'verbose_name': 'Изоброжение товара',
                'verbose_name_plural': 'Изоброжение товара',
            },
        ),
    ]
