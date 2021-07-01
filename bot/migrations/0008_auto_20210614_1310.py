# Generated by Django 3.2.4 on 2021-06-14 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_botuser_ban'),
        ('bot', '0007_alter_blog_articles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.botuser', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.botuser', verbose_name='Blog owner'),
        ),
        migrations.AlterField(
            model_name='blogsubscribers',
            name='subscriber',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.botuser', verbose_name='Blog subscriber'),
        ),
    ]