# Generated by Django 2.1.8 on 2019-09-10 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0003_goodstype_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='goods_description',
            field=models.TextField(default='Time goes by so fast, people go in and out of your life. You must never miss the opportunity to tell these people how much they mean to you.'),
        ),
    ]