# Generated by Django 3.2.6 on 2022-06-26 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=60)),
                ('LastName', models.CharField(max_length=60)),
                ('CIN', models.CharField(max_length=60)),
                ('Tel', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Age', models.IntegerField()),
                ('CreatedAt', models.DateField()),
                ('Picture', models.FileField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=60)),
                ('Email', models.EmailField(max_length=254)),
                ('Subject', models.CharField(max_length=255)),
                ('Message', models.TextField()),
                ('Seen', models.BooleanField()),
                ('CreatedAt', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Period', models.CharField(max_length=255)),
                ('Percentage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=60)),
                ('Type', models.CharField(choices=[('', ''), ('', ''), ('', ''), ('', ''), ('', ''), ('', ''), ('', '')], max_length=60)),
                ('BuyDate', models.DateField()),
                ('UseDate', models.DateField()),
                ('Picture', models.FileField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=60)),
                ('Localisation', models.CharField(max_length=255)),
                ('IsOpen', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartDate', models.DateField()),
                ('Duration', models.CharField(max_length=60)),
                ('EndSubscription', models.DateField()),
                ('SubscriptionPrice', models.FloatField()),
                ('ActiveInsurance', models.BooleanField()),
                ('IdClient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.client')),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=60)),
                ('LastName', models.CharField(max_length=60)),
                ('CIN', models.CharField(max_length=60)),
                ('Salary', models.IntegerField()),
                ('IdSalle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.salle')),
            ],
        ),
    ]
