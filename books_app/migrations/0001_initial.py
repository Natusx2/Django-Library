from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('publication_year', models.PositiveIntegerField()),
                ('genre', models.CharField(choices=[('classic', 'Classic'), ('fiction', 'Fiction'), ('dystopian', 'Dystopian'), ('romance', 'Romance'), ('fantasy', 'Fantasy'), ('science fiction', 'Science Fiction')], max_length=50)),
                ('available_copies', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
