from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
