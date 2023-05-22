# Generated by Django 4.2.1 on 2023-05-14 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('otp', models.IntegerField()),
                ('role', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('is_varified', models.BooleanField(default=False)),
                ('is_created', models.DateTimeField(auto_now_add=True)),
                ('is_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('logo_pic', models.ImageField(upload_to='app/img/company')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usermaster')),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('dob', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('min_salary', models.BigIntegerField()),
                ('max_salary', models.BigIntegerField()),
                ('job_type', models.CharField(max_length=150)),
                ('jobcategory', models.CharField(max_length=150)),
                ('education', models.CharField(max_length=150)),
                ('experiance', models.CharField(max_length=150)),
                ('jondescription', models.CharField(max_length=500)),
                ('profile_pic', models.ImageField(upload_to='app/img/candidate')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usermaster')),
            ],
        ),
    ]
