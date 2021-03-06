# Generated by Django 2.2.1 on 2019-05-04 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ColegioClasificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='EstudianteEstadoCivil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EstudianteEstrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EstudianteGenero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EstudianteNacionalidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EstudiantePerteneceMinoriaEtnica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EstudianteTieneDiscapacidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EstudianteTieneFinanciacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('estudianteEdad', models.IntegerField(blank=True, null=True)),
                ('estudianteEstadoCivil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recomendaciones.EstudianteEstadoCivil')),
                ('estudianteEstrato', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recomendaciones.EstudianteEstrato')),
                ('estudianteGenero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recomendaciones.EstudianteGenero')),
                ('estudianteNacionalidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recomendaciones.EstudianteNacionalidad')),
                ('estudiantePerteneceMinoriaEtnica', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recomendaciones.EstudiantePerteneceMinoriaEtnica')),
                ('estudianteTieneDiscapacidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recomendaciones.EstudianteTieneDiscapacidad')),
                ('estudianteTieneFinanciacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recomendaciones.EstudianteTieneFinanciacion')),
            ],
        ),
    ]
