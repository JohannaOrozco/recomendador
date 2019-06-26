from django.db import models

# Create your models here.

class EstudianteNacionalidad (models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre)

class EstudianteGenero (models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre)

class EstudianteEstadoCivil (models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre)

class EstudianteEstrato (models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre)

class EstudianteTieneFinanciacion (models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre)

class EstudiantePerteneceMinoriaEtnica (models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre)

class EstudianteTieneDiscapacidad (models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre)

class ColegioClasificacion(models.Model):
	nombre = models.CharField(max_length=2)

	def __str__(self):
		return '{}'.format(self.nombre)

class Estudiante(models.Model):

	# Datos del Estudiante
	nombre = models.CharField(max_length=100,
		blank=True,
        null=True)
	email = models.EmailField()

	estudianteNacionalidad = models.ForeignKey(EstudianteNacionalidad, 
		null = True, blank=True, on_delete=models.CASCADE)
	estudianteEdad = models.IntegerField(blank=True,
        null=True)
	estudianteGenero = models.ForeignKey(EstudianteGenero,
		blank=True, null=True, on_delete=models.CASCADE) 
	estudianteEstadoCivil = models.ForeignKey(EstudianteEstadoCivil,
		blank=True, null=True, on_delete=models.CASCADE)
	estudianteEstrato = models.ForeignKey(EstudianteEstrato,
		blank=True, null=True, on_delete=models.CASCADE)
	estudianteTieneFinanciacion = models.ForeignKey(EstudianteTieneFinanciacion,
		blank=True, null=True, on_delete=models.CASCADE)
	estudiantePerteneceMinoriaEtnica = models.ForeignKey(EstudiantePerteneceMinoriaEtnica,
		blank=True, null=True, on_delete=models.CASCADE)
	estudianteTieneDiscapacidad = models.ForeignKey(EstudianteTieneDiscapacidad,
		blank=True, null=True, on_delete=models.CASCADE)


	# # Datos del examen del icfes 'saber 11'
	# icfesAnoPresentacion = models.IntegerField()
	# icfesPeriodoPresentacion = models.DateField()
	# icfesPuntajeGlobal = models.IntegerField()
	# icfesPuntajeSocialesYCiudadanas = models.IntegerField()
	# icfesPuntajeLecturaCritica = models.IntegerField()
	# icfesPuntajeMatematicas = models.IntegerField()
	# icfesPuntajeCienciasNaturales = models.IntegerField()
	# icfesPuntajeIngles = models.IntegerField()


	# # Datos del Colegio 
	# colegioDepartamento = models.CharField(max_length=100)
	# colegioSector = models.CharField(max_length=100)
	# colegioZona = models.CharField(max_length=100)
	# colegioGenero = models.CharField(max_length=100)
	# colegioCaracter = models.CharField(max_length=100)
	# colegioCalendario = models.DateField()
	# colegioClasificacion = models.ManyToManyField(ColegioClasificacion)
	# colegioFueElMismo = models.CharField(max_length=100)


	# # Datos de los Padres 	
	# padresEstadoCivil = models.CharField(max_length=100)
	# madreNivelEducativo = models.CharField(max_length=100)
	# padreNivelEducativo = models.CharField(max_length=100)
	# madreOcupacion = models.CharField(max_length=100)
	# padreOcupacion = models.CharField(max_length=100)

	def __str__(self):
		return '{}'.format(self.nombre)





