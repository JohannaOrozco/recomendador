from django import forms

from recomendaciones.models import Estudiante

class EstudianteForm(forms.ModelForm):
	# nombre = forms.CharField(max_length=100, required=False, help_text='100 characters max.')
	# colegioZona = forms.CharField(max_length=100)
	# title = forms.CharField(
	# 	max_length=3,
	# 	widget=forms.Select(choices=TITLE_CHOICES),
	# 	)
    # birth_date = forms.DateField(required=False)

    # Datos del Estudiante
	# nombre = forms.CharField(max_length=100, required=False)
	# email = forms.EmailField()
	# estudianteNacionalidad = forms.CheckboxInput()
	# estudianteEdad = forms.IntegerField(required=False)
	# estudianteGenero = forms.CharField(max_length=100, required=False) 
	# estudianteEstadoCivil = forms.CharField(max_length=100, required=False)
	# estudianteEstrato = forms.CharField(max_length=100, required=False)
	# estudianteTieneFinanciacion = forms.CharField(max_length=100, required=False)
	# estudiantePerteneceMinoriaEtnica = forms.CharField(max_length=100, required=False)
	# estudianteTieneDiscapacidad = forms.CharField(max_length=100, required=False)


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

	class Meta:
		model = Estudiante

		fields = [
			'nombre',
			'email',
			'estudianteNacionalidad',
			'estudianteEdad',
			'estudianteGenero',
			'estudianteEstadoCivil',
			'estudianteEstrato',
			'estudianteTieneFinanciacion',
			'estudiantePerteneceMinoriaEtnica',
			'estudianteTieneDiscapacidad',
		]

		

		labels = {

			'nombre': 'Nombre',
			'email' : 'email',
			'estudianteNacionalidad' : 'Nacionalidad',
			'estudianteEdad' : 'Edad',
			'estudianteGenero' : 'Genero',
			'estudianteEstadoCivil' : 'Estado Civil',
			'estudianteEstrato' : 'Estrato',
			'estudianteTieneFinanciacion' : '¿Cuenta con financiacion?',
			'estudiantePerteneceMinoriaEtnica' : '¿Pertenece a una minoria etnica?',
			'estudianteTieneDiscapacidad' : '¿Tiene alguna discapacidad?',

		}

		widgets = {
			'nombre' : forms.TextInput(attrs={'class' : "col-lg-12",
				'class' : 'form-control',
				'id' : "inputDefault", 'placeholder' : "Nombres y Apellidos"}),
			'email': forms.TextInput(attrs={'class' : 'form-control', 
				'id' : "exampleInputEmail1", 'aria-describedby' : "emailHelp"
				,'placeholder' : "Ingrese su email"}),
			'estudianteNacionalidad' : forms.Select(attrs={ 'class' : "col-lg-4",
				'class' : 'form-control'}),
			'estudianteEdad' : forms.NumberInput(attrs={'class' : 'form-control'}),
			'estudianteGenero' : forms.Select(attrs={'class' : 'form-control'}),
			'estudianteEstadoCivil' : forms.Select(attrs={'class' : 'form-control'}),
			'estudianteEstrato' : forms.Select(attrs={'class' : 'form-control'}),
			'estudianteTieneFinanciacion' : forms.Select(attrs={'class' : 'form-control'}),
			'estudiantePerteneceMinoriaEtnica' : forms.Select(attrs={'class' : 'form-control'}),
			'estudianteTieneDiscapacidad' : forms.Select(attrs={'class' : 'form-control'}),

		}

	


