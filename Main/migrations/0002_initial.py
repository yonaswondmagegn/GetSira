# Generated by Django 4.2.2 on 2023-06-18 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profile', '0001_initial'),
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sira',
            name='recruiter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Profile.profile'),
        ),
        migrations.AddField(
            model_name='sira',
            name='set_of_skills',
            field=models.ManyToManyField(related_name='set_of_skills', to='Profile.skill'),
        ),
        migrations.AddField(
            model_name='sira',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Main.siratype'),
        ),
        migrations.AddField(
            model_name='aplication',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Profile.profile'),
        ),
        migrations.AddField(
            model_name='aplication',
            name='sira',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Main.sira'),
        ),
    ]
