# Generated by Django 2.2.13 on 2023-04-30 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forest_department_login',
            old_name='Designation1',
            new_name='Designation',
        ),
        migrations.RenameField(
            model_name='forest_department_login',
            old_name='email',
            new_name='Email',
        ),
    ]