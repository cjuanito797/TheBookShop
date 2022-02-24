# Generated by Django 4.0.2 on 2022-02-23 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
        ('accounts', '0002_user_favorite_authors_user_favorite_books_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favorite_authors',
            field=models.ManyToManyField(blank=True, related_name='favorite_authors', to='library.Author'),
        ),
        migrations.AlterField(
            model_name='user',
            name='favorite_books',
            field=models.ManyToManyField(blank=True, related_name='favorite_books', to='library.Book'),
        ),
        migrations.AlterField(
            model_name='user',
            name='favorite_genres',
            field=models.ManyToManyField(blank=True, related_name='favorite_genres', to='library.Genre'),
        ),
    ]
