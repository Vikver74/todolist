# Generated by Django 4.0.1 on 2022-12-07 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0006_alter_goal_user_alter_goalcategory_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goalcomment',
            name='goal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='goals.goal'),
        ),
    ]
