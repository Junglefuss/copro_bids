# Generated by Django 2.2.7 on 2019-11-06 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('copro_bids', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='public_profile_urls',
            new_name='website_urls',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='team_members',
        ),
        migrations.CreateModel(
            name='Teammate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('img_url', models.URLField()),
                ('role', models.CharField(max_length=100)),
                ('years_experience', models.DecimalField(decimal_places=0, max_digits=2)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=50)),
                ('public_profile_urls', models.TextField(max_length=500)),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teammates', to='copro_bids.Bid')),
            ],
        ),
    ]
