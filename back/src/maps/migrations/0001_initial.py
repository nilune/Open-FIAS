# Generated by Django 2.1.7 on 2019-03-16 20:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='имя объекта')),
                ('is_archive', models.BooleanField(default=False, verbose_name='объект в архиве')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='время обновления')),
                ('latitude', models.FloatField(verbose_name='широта')),
                ('longitude', models.FloatField(verbose_name='долгота')),
                ('country', models.CharField(max_length=255, verbose_name='страна')),
                ('region', models.CharField(blank=True, max_length=255, verbose_name='регион')),
                ('subregion', models.CharField(blank=True, max_length=255, verbose_name='под-регион')),
                ('locality', models.CharField(blank=True, max_length=255, verbose_name='населенный пункт')),
                ('suburb', models.CharField(blank=True, max_length=255, verbose_name='район города')),
                ('street', models.CharField(blank=True, max_length=255, verbose_name='название улицы')),
                ('building', models.CharField(blank=True, max_length=255, verbose_name='номер дома')),
                ('rank', models.IntegerField(blank=True, null=True, verbose_name='уровень адресного объекта')),
                ('postcode', models.IntegerField(blank=True, null=True, verbose_name='почтовый индекс')),
                ('author', models.ForeignKey(related_name='maps', on_delete=models.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='автор')),
            ],
            options={
                'verbose_name': 'Объект',
                'verbose_name_plural': 'Объекты',
                'ordering': ['country', 'region', 'subregion', 'locality', 'suburb', 'street', 'building'],
            },
        ),
    ]