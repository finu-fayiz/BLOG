# Generated by Django 4.2.3 on 2023-07-04 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=25, unique=True)),
                ('Mobile', models.CharField(max_length=10, unique=True)),
                ('Username', models.CharField(max_length=25, unique=True)),
                ('Password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ProfilePicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='upload')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.user_signup')),
            ],
        ),
    ]
