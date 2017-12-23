# Generated by Django 2.0 on 2017-12-22 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='message',
            field=models.CharField(blank=True, help_text="It's good to add some friendly message!", max_length=300, verbose_name='Optional message'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='to_user',
            field=models.ForeignKey(help_text='Please select the user you want to play a game with.', on_delete=django.db.models.deletion.CASCADE, related_name='invitations_received', to=settings.AUTH_USER_MODEL, verbose_name='User to invite'),
        ),
    ]
