# Generated by Django 5.0.1 on 2024-02-29 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theses', '0003_alter_student_unique_together_alter_student_thesis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='thesis',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='students', to='theses.thesis'),
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together={('user_ptr', 'thesis')},
        ),
    ]
