# Generated by Django 4.0 on 2021-12-25 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='static\\images')),
                ('description', models.TextField(max_length=600)),
                ('rate', models.PositiveIntegerField()),
                ('video', models.URLField(max_length=500)),
                ('trailer', models.URLField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=400)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='aflamna.film')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='auth.user')),
            ],
        ),
    ]
