# Generated by Django 2.2.7 on 2019-12-16 19:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0006_auto_20191129_0418'),
        ('students', '0011_remove_student_last_gpa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('initial', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='course.Course')),
            ],
        ),
        migrations.CreateModel(
            name='DailyAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_present', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='students.Student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='teachers.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='CourseAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('course', models.ManyToManyField(to='course.Course')),
                ('student', models.ManyToManyField(to='students.Student')),
                ('teacher', models.ManyToManyField(to='teachers.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='CourseAssignToTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ManyToManyField(to='course.Course')),
                ('teacher', models.ManyToManyField(to='teachers.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='CourseAssignToStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ManyToManyField(to='course.Course')),
                ('student', models.ManyToManyField(to='students.Student')),
            ],
        ),
    ]
