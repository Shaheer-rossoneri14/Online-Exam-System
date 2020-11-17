# Generated by Django 2.0 on 2018-02-25 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.CharField(max_length=50)),
                ('ans1', models.CharField(max_length=50)),
                ('ans2', models.CharField(max_length=50)),
                ('ans3', models.CharField(max_length=50)),
                ('ans4', models.CharField(max_length=50)),
                ('ans', models.CharField(max_length=50)),
                ('sub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quiz.Subject')),
            ],
        ),
    ]
