

class Usuario(object):
	"""Estructura de datos del Usuario"""
	def __init__(self, rawdata):
		# super(Usuario, self).__init__()

		self.rawdata = rawdata
		self.colegioDepartamento = None
		self.colegioSector = None
		self.colegioZona = None
		self.colegioGenero = None
		self.colegioCaracter = None
		self.colegioCalendario = None
		self.colegioClasificacion = None
		self.colegioFueElMismo = None
		self.estudianteNacionalidad = None
		
		self.icfesAnoPresentacion = None
		self.icfesPeriodoPresentacion = None

		self.icfesPuntajeGlobal = None

		self.icfesPuntajeSocialesYCiudadanas = None
		self.icfesPuntajeLecturaCritica = None
		self.icfesPuntajeMatematicas = None
		self.icfesPuntajeCienciasNaturales = None
		self.icfesPuntajeIngles = None

		self.estudianteEdad = None
		self.estudianteGenero = None
		self.estudianteEstadoCivil = None
		self.estudianteEstrato = None
		self.estudianteTieneFinanciacion = None
		self.padresEstadoCivil = None
		self.madreNivelEducativo = None
		self.padreNivelEducativo = None
		self.madreOcupacion = None
		self.padreOcupacion = None
		self.estudiantePerteneceMinoriaEtnica = None
		self.estudianteTieneDiscapacidad = None


		self.format_rawdata(self.rawdata)

		# Datos que utiliza el modelo
		self.PUNTAJE_GLOBAL = None
		self.EDAD_INGRESO = None
		self.APOYO_FINANCIERO = None
		self.EGRESADOS_COL_PERIODO = None
		self.CLASIFICACION_  = None
		self.CLASIFICACION_A = None
		self.CLASIFICACION_A_MAS = None
		self.CLASIFICACION_B = None
		self.CLASIFICACION_C = None
		self.CLASIFICACION_D = None
		self.DEPARTAMENTO_COLEGIO_AMAZONAS = None
		self.DEPARTAMENTO_COLEGIO_ANTIOQUIA = None
		self.DEPARTAMENTO_COLEGIO_ARAUCA = None
		self.DEPARTAMENTO_COLEGIO_ARCHIPIELAGO = None
		self.DEPARTAMENTO_COLEGIO_ATLANTICO = None
		self.DEPARTAMENTO_COLEGIO_BOGOTA = None
		self.DEPARTAMENTO_COLEGIO_BOLIVAR = None
		self.DEPARTAMENTO_COLEGIO_BOYACA = None
		self.DEPARTAMENTO_COLEGIO_CALDAS = None
		self.DEPARTAMENTO_COLEGIO_CAQUETA = None
		self.DEPARTAMENTO_COLEGIO_CASANARE = None
		self.DEPARTAMENTO_COLEGIO_CAUCA = None
		self.DEPARTAMENTO_COLEGIO_CESAR = None
		self.DEPARTAMENTO_COLEGIO_CHOCO = None
		self.DEPARTAMENTO_COLEGIO_CUNDINAMARCA = None
		self.DEPARTAMENTO_COLEGIO_CORDOBA = None
		self.DEPARTAMENTO_COLEGIO_GUAINIA = None
		self.DEPARTAMENTO_COLEGIO_GUAVIARE = None
		self.DEPARTAMENTO_COLEGIO_HUILA = None
		self.DEPARTAMENTO_COLEGIO_GUAJIRA = None
		self.DEPARTAMENTO_COLEGIO_MAGDALENA = None
		self.DEPARTAMENTO_COLEGIO_META = None
		self.DEPARTAMENTO_COLEGIO_NARINO = None
		self.DEPARTAMENTO_COLEGIO_NORTE_SANTANDER = None
		self.DEPARTAMENTO_COLEGIO_PUTUMAYO = None
		self.DEPARTAMENTO_COLEGIO_QUINDIO = None
		self.DEPARTAMENTO_COLEGIO_RISARALDA = None
		self.DEPARTAMENTO_COLEGIO_SANTANDER = None
		self.DEPARTAMENTO_COLEGIO_SUCRE = None
		self.DEPARTAMENTO_COLEGIO_TOLIMA = None
		self.DEPARTAMENTO_COLEGIO_VALLE = None
		self.DEPARTAMENTO_COLEGIO_VAUPES = None
		self.DEPARTAMENTO_COLEGIO_VICHADA = None
		self.SECTOR_COLEGIO_NO_OFICIAL = None
		self.SECTOR_COLEGIO_OFICIAL = None
		self.ZONA_COLEGIO_RURAL = None
		self.ZONA_COLEGIO_RURAL_URBANA = None
		self.ZONA_COLEGIO_URBANA = None
		self.ZONA_COLEGIO_URBANA_RURAL = None
		self.GENERO_COLEGIO_FEMENINO = None
		self.GENERO_COLEGIO_MASCULINO = None
		self.GENERO_COLEGIO_MIXTO = None
		self.CARACTER_COLEGIO_ACADEMICO = None
		self.CARACTER_COLEGIO_NO_APLICA = None
		self.CARACTER_COLEGIO_TECNICO = None
		self.CARACTER_COLEGIO_TECNICO_ACADEMICO = None
		self.CALENDARIO_COLEGIO_A = None
		self.CALENDARIO_COLEGIO_B = None
		self.CALENDARIO_COLEGIO_OTRO = None
		self.CURSO_COLEGIO_NO = None
		self.CURSO_COLEGIO_SI = None
		self.NACIONALIDAD_CO = None
		self.NACIONALIDAD_EX = None
		self.GENERO_F = None
		self.GENERO_M = None
		self.GENERO_N = None
		self.ESTADO_CIVIL_CASADO = None
		self.ESTADO_CIVIL_DIVORCIADO = None
		self.ESTADO_CIVIL_NO_DEFINIDO = None
		self.ESTADO_CIVIL_OTRO = None
		self.ESTADO_CIVIL_SEPARADO = None
		self.ESTADO_CIVIL_SOLTERO = None
		self.ESTADO_CIVIL_VIUDO = None
		self.ESTRATO_0 = None
		self.ESTRATO_1 = None
		self.ESTRATO_2 = None
		self.ESTRATO_3 = None
		self.ESTRATO_4 = None
		self.ESTRATO_5 = None
		self.ESTRATO_6 = None
		self.ESTADO_CIVIL_PADRES_CASADOS = None
		self.ESTADO_CIVIL_PADRES_DIVORCIADOS = None
		self.ESTADO_CIVIL_PADRES_O = None
		self.ESTADO_CIVIL_PADRES_SEPARADOS = None
		self.ESTADO_CIVIL_PADRES_SIN_INFO = None
		self.ESTADO_CIVIL_PADRES_SOLTERO = None
		self.ESTADO_CIVIL_PADRES_UNION_LIBRE = None
		self.ESTADO_CIVIL_PADRES_VIUDO = None
		self.NIVEL_EDU_MADRE_BACHILLERATO = None
		self.NIVEL_EDU_MADRE_POSTGRADO = None
		self.NIVEL_EDU_MADRE_PRIMARIA = None
		self.NIVEL_EDU_MADRE_PROFESIONAL = None
		self.NIVEL_EDU_MADRE_SIN_INFO = None
		self.NIVEL_EDU_MADRE_TECNICO = None
		self.NIVEL_EDU_PADRE_BACHILLERATO = None
		self.NIVEL_EDU_PADRE_POSTGRADO = None
		self.NIVEL_EDU_PADRE_PRIMARIA = None
		self.NIVEL_EDU_PADRE_PROFESIONAL = None
		self.NIVEL_EDU_PADRE_SIN_INFO = None
		self.NIVEL_EDU_PADRE_TECNICO = None
		self.OCUPACION_MADRE_DESEMPLEADA = None
		self.OCUPACION_MADRE_EMPLEADA = None
		self.OCUPACION_MADRE_EMPRESARIA = None
		self.OCUPACION_MADRE_INDEPENDIENTE = None
		self.OCUPACION_MADRE_OTRO = None
		self.OCUPACION_MADRE_SIN_INFO = None
		self.OCUPACION_PADRE_DESEMPLEADA = None
		self.OCUPACION_PADRE_EMPLEADA = None
		self.OCUPACION_PADRE_EMPRESARIA = None
		self.OCUPACION_PADRE_INDEPENDIENTE = None
		self.OCUPACION_PADRE_OTRO = None
		self.OCUPACION_PADRE_SIN_INFO = None
		self.MINORIA_ETNICA_NO = None
		self.MINORIA_ETNICA_SIN_INFO = None
		self.MINORIA_ETNICA_SI = None
		self.DISCAPACIDAD_FISICA_NO = None
		self.DISCAPACIDAD_FISICA_SIN_INFO = None
		self.DISCAPACIDAD_FISICA_SI = None

		self.format_data_model()

        
	
	def format_rawdata(self, rawdata):
		'Se toman los datos que llegan en la interface como un string separado por comas y se asigna a cada uno de los atributos'

		# Se crea el arreglo

		my_string = self.rawdata
		result = [x.strip() for x in my_string.split(',')]

		# Se asignan los valores a cada uno de los atributos que se estan tomando por la interface grafica

		self.colegioDepartamento = int(result[0]) #11
		self.colegioSector = result[1] #NO OFICIAL
		self.colegioZona = result[2] #URBANA
		self.colegioGenero = result[3] # MIXTO
		self.colegioCaracter = result[4] # ACADEMICO
		self.colegioCalendario = result[5] # B
		self.colegioClasificacion = result[6] #A+
		self.colegioFueElMismo = result[7] #SI
		self.estudianteNacionalidad = result[8] #CO

		self.icfesAnoPresentacion = result[9]  #2017
		self.icfesPeriodoPresentacion = result[10] #1

		self.icfesPuntajeGlobal = result[11] #80

		self.icfesPuntajeSocialesYCiudadanas = result[12] #70
		self.icfesPuntajeLecturaCritica = result[13] #80
		self.icfesPuntajeMatematicas = result[14]
		self.icfesPuntajeCienciasNaturales = result[15]
		self.icfesPuntajeIngles = result[16] #60

		self.estudianteEdad = result[17] #17
		self.estudianteGenero = result[18] #N
		self.estudianteEstadoCivil = result[19] #SOLTERO
		self.estudianteEstrato = result[20]  #4
		self.estudianteTieneFinanciacion = result[21] #NO
		self.padresEstadoCivil = result[22] # CASADOS
		self.madreNivelEducativo = result[23] # TECNICO
		self.padreNivelEducativo = result[24] # BACHILLERATO
		self.madreOcupacion = result[25] # EMPLEADA   
		self.padreOcupacion = result[26] # INDEPENDIENTE 
		self.estudiantePerteneceMinoriaEtnica = result[27] # NO
		self.estudianteTieneDiscapacidad = result[28] # NO


	def format_data_model(self):
		'Se asignan los valores a las variables de entrada definidas para correr el modelo'

		# Puntaje Global del Icfes del Estudiante

		self.PUNTAJE_GLOBAL = int(self.icfesPuntajeGlobal)

		print ('falta implementar self.icfesPuntajeSocialesYCiudadanas para que lo tome el modelo')
		print ('falta implementar self.icfesPuntajeLecturaCritica para que lo tome el modelo')
		print ('falta implementar self.icfesPuntajeMatematicas para que lo tome el modelo')
		print ('falta implementar self.icfesPuntajeCienciasNaturales para que lo tome el modelo')
		print ('falta implementar self.icfesPuntajeIngles para que lo tome el modelo')

		# icfes Ano Presentacion

		print ('falta implementar self.icfesAnoPresentacion para que lo tome el modelo')

		# icfes Periodo Presentacion

		print ('falta implementar self.icfesPeriodoPresentacionpara que lo tome el modelo')

		# Edad de Ingreso
		self.EDAD_INGRESO = int(self.estudianteEdad)

		# Tiene financiacion

		if self.estudianteTieneFinanciacion == 'SI':
			self.APOYO_FINANCIERO = 1

		elif self.estudianteTieneFinanciacion == 'NO':
			self.APOYO_FINANCIERO = 0

		else:
			print ('No se ha recibido un valor valido de apoyo financiero {}'.format(self.estudianteTieneFinanciacion))


		# Numero de Estudiantes egresados del colegio en el mismo periodo

		self.EGRESADOS_COL_PERIODO = 0

		# Clasificacion del colegio pendiente por implementar

		if self.colegioClasificacion == 'A':
			self.CLASIFICACION_  = 0
			self.CLASIFICACION_A = 1
			self.CLASIFICACION_A_MAS = 0
			self.CLASIFICACION_B = 0
			self.CLASIFICACION_C = 0
			self.CLASIFICACION_D = 0

		elif self.colegioClasificacion == 'A+':
			self.CLASIFICACION_  = 0
			self.CLASIFICACION_A = 0
			self.CLASIFICACION_A_MAS = 1
			self.CLASIFICACION_B = 0
			self.CLASIFICACION_C = 0
			self.CLASIFICACION_D = 0

		elif self.colegioClasificacion == 'B':
			self.CLASIFICACION_  = 0
			self.CLASIFICACION_A = 0
			self.CLASIFICACION_A_MAS == 0
			self.CLASIFICACION_B = 1
			self.CLASIFICACION_C = 0
			self.CLASIFICACION_D = 0

		elif self.colegioClasificacion == 'C':
			self.CLASIFICACION_  = 0
			self.CLASIFICACION_A = 0
			self.CLASIFICACION_A_MAS = 0
			self.CLASIFICACION_B = 0
			self.CLASIFICACION_C = 1
			self.CLASIFICACION_D = 0

		elif self.colegioClasificacion == 'D':
			self.CLASIFICACION_  = 0
			self.CLASIFICACION_A = 0
			self.CLASIFICACION_A_MAS = 0
			self.CLASIFICACION_B = 0
			self.CLASIFICACION_C = 0
			self.CLASIFICACION_D = 1

		else:
			print ('No se ha recibido una Clasificacion de colegio valida {}'.format(self.colegioClasificacion))

		# Colegio departamento esta pendiente cambiarlo al codigo DANE

		self.DEPARTAMENTO_COLEGIO_AMAZONAS = self.colegioDepartamento
		self.DEPARTAMENTO_COLEGIO_ANTIOQUIA = 0
		self.DEPARTAMENTO_COLEGIO_ARAUCA = 0
		self.DEPARTAMENTO_COLEGIO_ARCHIPIELAGO = 0
		self.DEPARTAMENTO_COLEGIO_ATLANTICO = 0
		self.DEPARTAMENTO_COLEGIO_BOGOTA = 0
		self.DEPARTAMENTO_COLEGIO_BOLIVAR = 0
		self.DEPARTAMENTO_COLEGIO_BOYACA = 0
		self.DEPARTAMENTO_COLEGIO_CALDAS = 0
		self.DEPARTAMENTO_COLEGIO_CAQUETA = 0
		self.DEPARTAMENTO_COLEGIO_CASANARE = 0
		self.DEPARTAMENTO_COLEGIO_CAUCA = 0
		self.DEPARTAMENTO_COLEGIO_CESAR = 0
		self.DEPARTAMENTO_COLEGIO_CHOCO = 0
		self.DEPARTAMENTO_COLEGIO_CUNDINAMARCA = 0
		self.DEPARTAMENTO_COLEGIO_CORDOBA = 0
		self.DEPARTAMENTO_COLEGIO_GUAINIA = 0
		self.DEPARTAMENTO_COLEGIO_GUAVIARE = 0
		self.DEPARTAMENTO_COLEGIO_HUILA = 0
		self.DEPARTAMENTO_COLEGIO_GUAJIRA = 0
		self.DEPARTAMENTO_COLEGIO_MAGDALENA = 0
		self.DEPARTAMENTO_COLEGIO_META = 0
		self.DEPARTAMENTO_COLEGIO_NARINO = 0
		self.DEPARTAMENTO_COLEGIO_NORTE_SANTANDER = 0
		self.DEPARTAMENTO_COLEGIO_PUTUMAYO = 0
		self.DEPARTAMENTO_COLEGIO_QUINDIO = 0
		self.DEPARTAMENTO_COLEGIO_RISARALDA = 0
		self.DEPARTAMENTO_COLEGIO_SANTANDER = 0
		self.DEPARTAMENTO_COLEGIO_SUCRE = 0
		self.DEPARTAMENTO_COLEGIO_TOLIMA = 0
		self.DEPARTAMENTO_COLEGIO_VALLE = 0
		self.DEPARTAMENTO_COLEGIO_VAUPES = 0
		self.DEPARTAMENTO_COLEGIO_VICHADA = 0

		# Colegio Sector Oficial 

		if self.colegioSector == 'OFICIAL':
			self.SECTOR_COLEGIO_NO_OFICIAL = 0
			self.SECTOR_COLEGIO_OFICIAL = 1
		else:
			self.SECTOR_COLEGIO_NO_OFICIAL = 1
			self.SECTOR_COLEGIO_OFICIAL = 0

		# Zona colegio

		if self.colegioZona == 'RURAL':
			self.ZONA_COLEGIO_RURAL = 1
			self.ZONA_COLEGIO_RURAL_URBANA = 0
			self.ZONA_COLEGIO_URBANA = 0
			self.ZONA_COLEGIO_URBANA_RURAL = 0
		elif self.colegioZona == 'RURAL-URBANA':
			self.ZONA_COLEGIO_RURAL = 0
			self.ZONA_COLEGIO_RURAL_URBANA = 1
			self.ZONA_COLEGIO_URBANA = 0
			self.ZONA_COLEGIO_URBANA_RURAL = 0
		elif self.colegioZona == 'URBANA':
			self.ZONA_COLEGIO_RURAL = 0
			self.ZONA_COLEGIO_RURAL_URBANA = 0
			self.ZONA_COLEGIO_URBANA = 1
			self.ZONA_COLEGIO_URBANA_RURAL = 0
		elif self.colegioZona == 'URBANA-RURAL':
			self.ZONA_COLEGIO_RURAL = 0
			self.ZONA_COLEGIO_RURAL_URBANA = 0
			self.ZONA_COLEGIO_URBANA = 0
			self.ZONA_COLEGIO_URBANA_RURAL = 1
		else:
			print ('No se ha recibido una Zona de colegio valida {}'.format(self.colegioZona))

		# Genero del Colegio

		if self.colegioGenero == 'FEMENINO':
			self.GENERO_COLEGIO_FEMENINO = 1
			self.GENERO_COLEGIO_MASCULINO = 0
			self.GENERO_COLEGIO_MIXTO = 0

		elif self.colegioGenero == 'MASCULINO':
			self.GENERO_COLEGIO_FEMENINO = 0
			self.GENERO_COLEGIO_MASCULINO = 1
			self.GENERO_COLEGIO_MIXTO = 0

		elif self.colegioGenero == 'MIXTO':
			self.GENERO_COLEGIO_FEMENINO = 0
			self.GENERO_COLEGIO_MASCULINO = 0
			self.GENERO_COLEGIO_MIXTO = 1

		else:
			print('No se ha recibido un genero del Colegio valido {}'.format(self.colegioGenero))

		# Caracter del colegio

		if self.colegioCaracter == 'TECNICO':
			self.CARACTER_COLEGIO_ACADEMICO = 0
			self.CARACTER_COLEGIO_NO_APLICA = 0
			self.CARACTER_COLEGIO_TECNICO = 1
			self.CARACTER_COLEGIO_TECNICO_ACADEMICO = 0

		elif self.colegioCaracter == 'ACADEMICO':
			self.CARACTER_COLEGIO_ACADEMICO = 1
			self.CARACTER_COLEGIO_NO_APLICA = 0
			self.CARACTER_COLEGIO_TECNICO = 0
			self.CARACTER_COLEGIO_TECNICO_ACADEMICO = 0

		elif self.colegioCaracter == 'TECNICO/ACADEMICO':
			self.CARACTER_COLEGIO_ACADEMICO = 0
			self.CARACTER_COLEGIO_NO_APLICA = 0
			self.CARACTER_COLEGIO_TECNICO = 0
			self.CARACTER_COLEGIO_TECNICO_ACADEMICO = 1

		elif self.colegioCaracter == 'OTRO':
			self.CARACTER_COLEGIO_ACADEMICO = 0
			self.CARACTER_COLEGIO_NO_APLICA = 1
			self.CARACTER_COLEGIO_TECNICO = 0
			self.CARACTER_COLEGIO_TECNICO_ACADEMICO = 0

		else:
			print('No se ha recibido un caracter del Colegio valido {}'.format(self.colegioCaracter))


		# Calendario del colegio

		if self.colegioCalendario == 'A':
			self.CALENDARIO_COLEGIO_A = 1
			self.CALENDARIO_COLEGIO_B = 0
			self.CALENDARIO_COLEGIO_OTRO = 0

		elif self.colegioCalendario == 'B':
			self.CALENDARIO_COLEGIO_A = 0
			self.CALENDARIO_COLEGIO_B = 1
			self.CALENDARIO_COLEGIO_OTRO = 0

		elif self.colegioCalendario == 'OTRO':
			self.CALENDARIO_COLEGIO_A = 0
			self.CALENDARIO_COLEGIO_B = 0
			self.CALENDARIO_COLEGIO_OTRO = 1

		else:
			print('No se ha recibido un Calendario del Colegio valido {}'.format(self.colegioCalendario))

		# Fue al mismo colegio durante toda su epoca escolar

		if self.colegioFueElMismo =='SI':
			self.CURSO_COLEGIO_NO = 0
			self.CURSO_COLEGIO_SI = 1

		elif self.colegioFueElMismo =='NO':
			self.CURSO_COLEGIO_NO = 0
			self.CURSO_COLEGIO_SI = 1

		else:
			print('No se ha recibido un colegioFueElMismo valido {}'.format(self.colegioFueElMismo))
		
		
		# Nacionalidad del Estudiante

		if self.estudianteNacionalidad == 'CO':
			self.NACIONALIDAD_CO = 1
			self.NACIONALIDAD_EX = 0

		elif self.estudianteNacionalidad == 'EX':
			self.NACIONALIDAD_CO = 0
			self.NACIONALIDAD_EX = 1

		else:
			print('No se ha recibido una nacionalidad valida para el estudiante {}'.format(self.estudianteNacionalidad))

		# Genero del Estudiante

		if self.estudianteGenero == 'M':
			self.GENERO_F = 0
			self.GENERO_M = 1
			self.GENERO_N = 0

		elif self.estudianteGenero == 'F':
			self.GENERO_F = 1
			self.GENERO_M = 0
			self.GENERO_N = 0

		elif self.estudianteGenero == 'N':
			self.GENERO_F = 0
			self.GENERO_M = 0
			self.GENERO_N = 1

		else:
			print('No se ha recibido un genero valido para el estudiante {}'.format(self.estudianteGenero))

		# Estado civil del Estudiante


		if self.estudianteEstadoCivil == 'CASADO':
			self.ESTADO_CIVIL_CASADO = 1
			self.ESTADO_CIVIL_DIVORCIADO = 0
			self.ESTADO_CIVIL_NO_DEFINIDO = 0
			self.ESTADO_CIVIL_OTRO = 0
			self.ESTADO_CIVIL_SEPARADO = 0
			self.ESTADO_CIVIL_SOLTERO = 0
			self.ESTADO_CIVIL_VIUDO = 0

		# elif self.estudianteEstadoCivil == 'UNION LIBRE':
		# 	'No esta definido entre los datos falta ajustar el programa'
		# 	self.ESTADO_CIVIL_CASADO = 0
		# 	self.ESTADO_CIVIL_DIVORCIADO = 0
		# 	self.ESTADO_CIVIL_NO_DEFINIDO = 0
		# 	self.ESTADO_CIVIL_OTRO = 0
		# 	self.ESTADO_CIVIL_SEPARADO = 0
		# 	self.ESTADO_CIVIL_SOLTERO = 0
		# 	self.ESTADO_CIVIL_VIUDO = 0

		elif self.estudianteEstadoCivil == 'DIVORCIADO':
			self.ESTADO_CIVIL_CASADO = 0
			self.ESTADO_CIVIL_DIVORCIADO = 1
			self.ESTADO_CIVIL_NO_DEFINIDO = 0
			self.ESTADO_CIVIL_OTRO = 0
			self.ESTADO_CIVIL_SEPARADO = 0
			self.ESTADO_CIVIL_SOLTERO = 0
			self.ESTADO_CIVIL_VIUDO = 0

		elif self.estudianteEstadoCivil == 'SEPARADO':
			self.ESTADO_CIVIL_CASADO = 0
			self.ESTADO_CIVIL_DIVORCIADO = 0
			self.ESTADO_CIVIL_NO_DEFINIDO = 0
			self.ESTADO_CIVIL_OTRO = 0
			self.ESTADO_CIVIL_SEPARADO = 1
			self.ESTADO_CIVIL_SOLTERO = 0
			self.ESTADO_CIVIL_VIUDO = 0

		elif self.estudianteEstadoCivil == 'SOLTERO':
			self.ESTADO_CIVIL_CASADO = 0
			self.ESTADO_CIVIL_DIVORCIADO = 0
			self.ESTADO_CIVIL_NO_DEFINIDO = 0
			self.ESTADO_CIVIL_OTRO = 0
			self.ESTADO_CIVIL_SEPARADO = 0
			self.ESTADO_CIVIL_SOLTERO = 1
			self.ESTADO_CIVIL_VIUDO = 0

		elif self.estudianteEstadoCivil == 'VIUDO':
			self.ESTADO_CIVIL_CASADO = 0
			self.ESTADO_CIVIL_DIVORCIADO = 0
			self.ESTADO_CIVIL_NO_DEFINIDO = 0
			self.ESTADO_CIVIL_OTRO = 0
			self.ESTADO_CIVIL_SEPARADO = 0
			self.ESTADO_CIVIL_SOLTERO = 0
			self.ESTADO_CIVIL_VIUDO = 1

		elif self.estudianteEstadoCivil == 'OTRO':
			self.ESTADO_CIVIL_CASADO = 0
			self.ESTADO_CIVIL_DIVORCIADO = 0
			self.ESTADO_CIVIL_NO_DEFINIDO = 0
			self.ESTADO_CIVIL_OTRO = 1
			self.ESTADO_CIVIL_SEPARADO = 0
			self.ESTADO_CIVIL_SOLTERO = 0
			self.ESTADO_CIVIL_VIUDO = 0

		else:
			print('No se ha recibido un estado civil valido para el estudiante {} puede ser UNION LIBRE que no se ha implementado'
				.format(self.estudianteEstadoCivil))


		# Estrato del Estudiante

		if self.estudianteEstrato == str(0):
			self.ESTRATO_0 = 1
			self.ESTRATO_1 = 0
			self.ESTRATO_2 = 0
			self.ESTRATO_3 = 0
			self.ESTRATO_4 = 0
			self.ESTRATO_5 = 0
			self.ESTRATO_6 = 0

		elif self.estudianteEstrato == str(1):
			self.ESTRATO_0 = 0
			self.ESTRATO_1 = 1
			self.ESTRATO_2 = 0
			self.ESTRATO_3 = 0
			self.ESTRATO_4 = 0
			self.ESTRATO_5 = 0
			self.ESTRATO_6 = 0

		elif self.estudianteEstrato == str(2):
			self.ESTRATO_0 = 0
			self.ESTRATO_1 = 0
			self.ESTRATO_2 = 1
			self.ESTRATO_3 = 0
			self.ESTRATO_4 = 0
			self.ESTRATO_5 = 0
			self.ESTRATO_6 = 0

		elif self.estudianteEstrato == str(3):
			self.ESTRATO_0 = 0
			self.ESTRATO_1 = 0
			self.ESTRATO_2 = 0
			self.ESTRATO_3 = 1
			self.ESTRATO_4 = 0
			self.ESTRATO_5 = 0
			self.ESTRATO_6 = 0

		elif self.estudianteEstrato == str(4):
			self.ESTRATO_0 = 0
			self.ESTRATO_1 = 0
			self.ESTRATO_2 = 0
			self.ESTRATO_3 = 0
			self.ESTRATO_4 = 1
			self.ESTRATO_5 = 0
			self.ESTRATO_6 = 0

		elif self.estudianteEstrato == str(5):
			self.ESTRATO_0 = 0
			self.ESTRATO_1 = 0
			self.ESTRATO_2 = 0
			self.ESTRATO_3 = 0
			self.ESTRATO_4 = 0
			self.ESTRATO_5 = 1
			self.ESTRATO_6 = 0

		elif self.estudianteEstrato == str(6):
			self.ESTRATO_0 = 0
			self.ESTRATO_1 = 0
			self.ESTRATO_2 = 0
			self.ESTRATO_3 = 0
			self.ESTRATO_4 = 0
			self.ESTRATO_5 = 0
			self.ESTRATO_6 = 1

		else:
			print('No se ha recibido un Estrato valido para el estudiante {}'.format(self.estudianteEstrato))

		# Estado civil de los padres

		if self.padresEstadoCivil == 'CASADOS':
			self.ESTADO_CIVIL_PADRES_CASADOS = 1
			self.ESTADO_CIVIL_PADRES_DIVORCIADOS = 0
			self.ESTADO_CIVIL_PADRES_O = 0
			self.ESTADO_CIVIL_PADRES_SEPARADOS = 0
			self.ESTADO_CIVIL_PADRES_SIN_INFO = 0
			self.ESTADO_CIVIL_PADRES_SOLTERO = 0
			self.ESTADO_CIVIL_PADRES_UNION_LIBRE = 0
			self.ESTADO_CIVIL_PADRES_VIUDO = 0

		elif self.padresEstadoCivil == 'DIVORCIADOS':
			self.ESTADO_CIVIL_PADRES_CASADOS = 0
			self.ESTADO_CIVIL_PADRES_DIVORCIADOS = 1
			self.ESTADO_CIVIL_PADRES_O = 0
			self.ESTADO_CIVIL_PADRES_SEPARADOS = 0
			self.ESTADO_CIVIL_PADRES_SIN_INFO = 0
			self.ESTADO_CIVIL_PADRES_SOLTERO = 0
			self.ESTADO_CIVIL_PADRES_UNION_LIBRE = 0
			self.ESTADO_CIVIL_PADRES_VIUDO = 0

		elif self.padresEstadoCivil == 'SEPARADOS':
			self.ESTADO_CIVIL_PADRES_CASADOS = 0
			self.ESTADO_CIVIL_PADRES_DIVORCIADOS = 0
			self.ESTADO_CIVIL_PADRES_O = 0
			self.ESTADO_CIVIL_PADRES_SEPARADOS = 1
			self.ESTADO_CIVIL_PADRES_SIN_INFO = 0
			self.ESTADO_CIVIL_PADRES_SOLTERO = 0
			self.ESTADO_CIVIL_PADRES_UNION_LIBRE = 0
			self.ESTADO_CIVIL_PADRES_VIUDO = 0

		elif self.padresEstadoCivil == 'SOLTEROS':
			self.ESTADO_CIVIL_PADRES_CASADOS = 0
			self.ESTADO_CIVIL_PADRES_DIVORCIADOS = 0
			self.ESTADO_CIVIL_PADRES_O = 0
			self.ESTADO_CIVIL_PADRES_SEPARADOS = 0
			self.ESTADO_CIVIL_PADRES_SIN_INFO = 0
			self.ESTADO_CIVIL_PADRES_SOLTERO = 1
			self.ESTADO_CIVIL_PADRES_UNION_LIBRE = 0
			self.ESTADO_CIVIL_PADRES_VIUDO = 0

		elif self.padresEstadoCivil == 'UNION LIBRE':
			self.ESTADO_CIVIL_PADRES_CASADOS = 0
			self.ESTADO_CIVIL_PADRES_DIVORCIADOS = 0
			self.ESTADO_CIVIL_PADRES_O = 0
			self.ESTADO_CIVIL_PADRES_SEPARADOS = 0
			self.ESTADO_CIVIL_PADRES_SIN_INFO = 0
			self.ESTADO_CIVIL_PADRES_SOLTERO = 0
			self.ESTADO_CIVIL_PADRES_UNION_LIBRE = 1
			self.ESTADO_CIVIL_PADRES_VIUDO = 0

		elif self.padresEstadoCivil == 'VIUDOS':
			self.ESTADO_CIVIL_PADRES_CASADOS = 0
			self.ESTADO_CIVIL_PADRES_DIVORCIADOS = 0
			self.ESTADO_CIVIL_PADRES_O = 0
			self.ESTADO_CIVIL_PADRES_SEPARADOS = 0
			self.ESTADO_CIVIL_PADRES_SIN_INFO = 0
			self.ESTADO_CIVIL_PADRES_SOLTERO = 0
			self.ESTADO_CIVIL_PADRES_UNION_LIBRE = 0
			self.ESTADO_CIVIL_PADRES_VIUDO = 1

		elif self.padresEstadoCivil == 'OTRO':
			self.ESTADO_CIVIL_PADRES_CASADOS = 0
			self.ESTADO_CIVIL_PADRES_DIVORCIADOS = 0
			self.ESTADO_CIVIL_PADRES_O = 0
			self.ESTADO_CIVIL_PADRES_SEPARADOS = 0
			self.ESTADO_CIVIL_PADRES_SIN_INFO = 0
			self.ESTADO_CIVIL_PADRES_SOLTERO = 0
			self.ESTADO_CIVIL_PADRES_UNION_LIBRE = 0
			self.ESTADO_CIVIL_PADRES_VIUDO = 1

		else:
			print('No se ha recibido un estado civil de los padres valido {}'.format(self.padresEstadoCivil))


		# Nivel educativo de la madre

		if self.madreNivelEducativo == 'PRIMARIA':
			self.NIVEL_EDU_MADRE_BACHILLERATO = 0
			self.NIVEL_EDU_MADRE_POSTGRADO = 0
			self.NIVEL_EDU_MADRE_PRIMARIA = 1
			self.NIVEL_EDU_MADRE_PROFESIONAL = 0
			self.NIVEL_EDU_MADRE_SIN_INFO = 0
			self.NIVEL_EDU_MADRE_TECNICO = 0

		elif self.madreNivelEducativo == 'BACHILLERATO':
			self.NIVEL_EDU_MADRE_BACHILLERATO = 1
			self.NIVEL_EDU_MADRE_POSTGRADO = 0
			self.NIVEL_EDU_MADRE_PRIMARIA = 0
			self.NIVEL_EDU_MADRE_PROFESIONAL = 0
			self.NIVEL_EDU_MADRE_SIN_INFO = 0
			self.NIVEL_EDU_MADRE_TECNICO = 0

		elif self.madreNivelEducativo == 'TECNICO':
			self.NIVEL_EDU_MADRE_BACHILLERATO = 0
			self.NIVEL_EDU_MADRE_POSTGRADO = 0
			self.NIVEL_EDU_MADRE_PRIMARIA = 0
			self.NIVEL_EDU_MADRE_PROFESIONAL = 0
			self.NIVEL_EDU_MADRE_SIN_INFO = 0
			self.NIVEL_EDU_MADRE_TECNICO = 1

		elif self.madreNivelEducativo == 'PROFESIONAL':
			self.NIVEL_EDU_MADRE_BACHILLERATO = 0
			self.NIVEL_EDU_MADRE_POSTGRADO = 0
			self.NIVEL_EDU_MADRE_PRIMARIA = 0
			self.NIVEL_EDU_MADRE_PROFESIONAL = 1
			self.NIVEL_EDU_MADRE_SIN_INFO = 0
			self.NIVEL_EDU_MADRE_TECNICO = 0

		elif self.madreNivelEducativo == 'POSTGRADO':
			self.NIVEL_EDU_MADRE_BACHILLERATO = 0
			self.NIVEL_EDU_MADRE_POSTGRADO = 1
			self.NIVEL_EDU_MADRE_PRIMARIA = 0
			self.NIVEL_EDU_MADRE_PROFESIONAL = 0
			self.NIVEL_EDU_MADRE_SIN_INFO = 0
			self.NIVEL_EDU_MADRE_TECNICO = 0

		else:
			print('No se ha recibido un nivel educativo de la madre no valido {}'.format(self.madreNivelEducativo))

		# Nivel educativo del Padre

		if self.padreNivelEducativo == 'PRIMARIA':
			self.NIVEL_EDU_PADRE_BACHILLERATO = 0
			self.NIVEL_EDU_PADRE_POSTGRADO = 0
			self.NIVEL_EDU_PADRE_PRIMARIA = 1
			self.NIVEL_EDU_PADRE_PROFESIONAL = 0
			self.NIVEL_EDU_PADRE_SIN_INFO = 0
			self.NIVEL_EDU_PADRE_TECNICO = 0

		elif self.padreNivelEducativo == 'BACHILLERATO':
			self.NIVEL_EDU_PADRE_BACHILLERATO = 1
			self.NIVEL_EDU_PADRE_POSTGRADO = 0
			self.NIVEL_EDU_PADRE_PRIMARIA = 0
			self.NIVEL_EDU_PADRE_PROFESIONAL = 0
			self.NIVEL_EDU_PADRE_SIN_INFO = 0
			self.NIVEL_EDU_PADRE_TECNICO = 0	

		elif self.padreNivelEducativo == 'TECNICO':
			self.NIVEL_EDU_PADRE_BACHILLERATO = 0
			self.NIVEL_EDU_PADRE_POSTGRADO = 0
			self.NIVEL_EDU_PADRE_PRIMARIA = 0
			self.NIVEL_EDU_PADRE_PROFESIONAL = 0
			self.NIVEL_EDU_PADRE_SIN_INFO = 0
			self.NIVEL_EDU_PADRE_TECNICO = 1

		elif self.padreNivelEducativo == 'PROFESIONAL':
			self.NIVEL_EDU_PADRE_BACHILLERATO = 0
			self.NIVEL_EDU_PADRE_POSTGRADO = 0
			self.NIVEL_EDU_PADRE_PRIMARIA = 0
			self.NIVEL_EDU_PADRE_PROFESIONAL = 1
			self.NIVEL_EDU_PADRE_SIN_INFO = 0
			self.NIVEL_EDU_PADRE_TECNICO = 0

		elif self.padreNivelEducativo == 'POSTGRADO':
			self.NIVEL_EDU_PADRE_BACHILLERATO = 0
			self.NIVEL_EDU_PADRE_POSTGRADO = 1
			self.NIVEL_EDU_PADRE_PRIMARIA = 0
			self.NIVEL_EDU_PADRE_PROFESIONAL = 0
			self.NIVEL_EDU_PADRE_SIN_INFO = 0
			self.NIVEL_EDU_PADRE_TECNICO = 0	

		else:
			print('No se ha recibido un nivel educativo del padre no valido {}'.format(self.padreNivelEducativo))

		# Nivel ocupacion de la Madre

		if self.madreOcupacion == 'DESEMPLEADA':
			self.OCUPACION_MADRE_DESEMPLEADA = 1
			self.OCUPACION_MADRE_EMPLEADA = 0
			self.OCUPACION_MADRE_EMPRESARIA = 0
			self.OCUPACION_MADRE_INDEPENDIENTE = 0
			self.OCUPACION_MADRE_OTRO = 0
			self.OCUPACION_MADRE_SIN_INFO = 0

		elif self.madreOcupacion == 'EMPLEADA':
			self.OCUPACION_MADRE_DESEMPLEADA = 0
			self.OCUPACION_MADRE_EMPLEADA = 1
			self.OCUPACION_MADRE_EMPRESARIA = 0
			self.OCUPACION_MADRE_INDEPENDIENTE = 0
			self.OCUPACION_MADRE_OTRO = 0
			self.OCUPACION_MADRE_SIN_INFO = 0

		elif self.madreOcupacion == 'EMPRESARIA':
			self.OCUPACION_MADRE_DESEMPLEADA = 0
			self.OCUPACION_MADRE_EMPLEADA = 0
			self.OCUPACION_MADRE_EMPRESARIA = 1
			self.OCUPACION_MADRE_INDEPENDIENTE = 0
			self.OCUPACION_MADRE_OTRO = 0
			self.OCUPACION_MADRE_SIN_INFO = 0

		elif self.madreOcupacion == 'INDEPENDIENTE':
			self.OCUPACION_MADRE_DESEMPLEADA = 0
			self.OCUPACION_MADRE_EMPLEADA = 0
			self.OCUPACION_MADRE_EMPRESARIA = 0
			self.OCUPACION_MADRE_INDEPENDIENTE = 1
			self.OCUPACION_MADRE_OTRO = 0
			self.OCUPACION_MADRE_SIN_INFO = 0

		elif self.madreOcupacion == 'OTRO':
			self.OCUPACION_MADRE_DESEMPLEADA = 0
			self.OCUPACION_MADRE_EMPLEADA = 0
			self.OCUPACION_MADRE_EMPRESARIA = 0
			self.OCUPACION_MADRE_INDEPENDIENTE = 0
			self.OCUPACION_MADRE_OTRO = 1
			self.OCUPACION_MADRE_SIN_INFO = 0

		else:
			print('No se ha recibido una ocupacion valida para la madre {}'.format(self.madreOcupacion))

		# Nivel ocupacion del Padre

		if self.padreOcupacion == 'DESEMPLEADO':
			self.OCUPACION_PADRE_DESEMPLEADA = 1
			self.OCUPACION_PADRE_EMPLEADA = 0
			self.OCUPACION_PADRE_EMPRESARIA = 0
			self.OCUPACION_PADRE_INDEPENDIENTE = 0
			self.OCUPACION_PADRE_OTRO = 0
			self.OCUPACION_PADRE_SIN_INFO = 0

		elif self.padreOcupacion == 'EMPLEADO':
			self.OCUPACION_PADRE_DESEMPLEADA = 0
			self.OCUPACION_PADRE_EMPLEADA = 1
			self.OCUPACION_PADRE_EMPRESARIA = 0
			self.OCUPACION_PADRE_INDEPENDIENTE = 0
			self.OCUPACION_PADRE_OTRO = 0
			self.OCUPACION_PADRE_SIN_INFO = 0

		elif self.padreOcupacion == 'EMPRESARIO':
			self.OCUPACION_PADRE_DESEMPLEADA = 0
			self.OCUPACION_PADRE_EMPLEADA = 0
			self.OCUPACION_PADRE_EMPRESARIA = 1
			self.OCUPACION_PADRE_INDEPENDIENTE = 0
			self.OCUPACION_PADRE_OTRO = 0
			self.OCUPACION_PADRE_SIN_INFO = 0

		elif self.padreOcupacion == 'INDEPENDIENTE':
			self.OCUPACION_PADRE_DESEMPLEADA = 0
			self.OCUPACION_PADRE_EMPLEADA = 0
			self.OCUPACION_PADRE_EMPRESARIA = 0
			self.OCUPACION_PADRE_INDEPENDIENTE = 1
			self.OCUPACION_PADRE_OTRO = 0
			self.OCUPACION_PADRE_SIN_INFO = 0

		elif self.padreOcupacion == 'OTRO':
			self.OCUPACION_PADRE_DESEMPLEADA = 0
			self.OCUPACION_PADRE_EMPLEADA = 0
			self.OCUPACION_PADRE_EMPRESARIA = 0
			self.OCUPACION_PADRE_INDEPENDIENTE = 0
			self.OCUPACION_PADRE_OTRO = 1
			self.OCUPACION_PADRE_SIN_INFO = 0

		else:
			print('No se ha recibido una ocupacion valida para el padre {}'.format(self.padreOcupacion))

		# El estudiante pertenece a una minoria etnica

		if self.estudiantePerteneceMinoriaEtnica == 'SI':
			self.MINORIA_ETNICA_NO = 0
			self.MINORIA_ETNICA_SIN_INFO = 0
			self.MINORIA_ETNICA_SI = 1

		elif self.estudiantePerteneceMinoriaEtnica == 'NO':
			self.MINORIA_ETNICA_NO = 1
			self.MINORIA_ETNICA_SIN_INFO = 0
			self.MINORIA_ETNICA_SI = 0

		else:
			print('No se ha recibido un valor valido de minoria etnica para el estudiante {}'.format(self.estudiantePerteneceMinoriaEtnica))

		# El estudiante tiene una discapacidad

		if self.estudianteTieneDiscapacidad == 'SI':
			self.DISCAPACIDAD_FISICA_NO = 0
			self.DISCAPACIDAD_FISICA_SIN_INFO = 0
			self.DISCAPACIDAD_FISICA_SI = 1

		elif self.estudianteTieneDiscapacidad == 'NO':
			self.DISCAPACIDAD_FISICA_NO = 0
			self.DISCAPACIDAD_FISICA_SIN_INFO = 0
			self.DISCAPACIDAD_FISICA_SI = 1

		else:
			print('No se ha recibido un valor valido de discapacidad para el estudiante {}'.format(self.estudianteTieneDiscapacidad))


		inputData =[[

		self.PUNTAJE_GLOBAL,
		self.EDAD_INGRESO,
		self.APOYO_FINANCIERO,
		self.EGRESADOS_COL_PERIODO,
		self.CLASIFICACION_ ,
		self.CLASIFICACION_A,
		self.CLASIFICACION_A_MAS,
		self.CLASIFICACION_B,
		self.CLASIFICACION_C,
		self.CLASIFICACION_D,
		self.DEPARTAMENTO_COLEGIO_AMAZONAS,
		self.DEPARTAMENTO_COLEGIO_ANTIOQUIA,
		self.DEPARTAMENTO_COLEGIO_ARAUCA,
		self.DEPARTAMENTO_COLEGIO_ARCHIPIELAGO,
		self.DEPARTAMENTO_COLEGIO_ATLANTICO,
		self.DEPARTAMENTO_COLEGIO_BOGOTA,
		self.DEPARTAMENTO_COLEGIO_BOLIVAR,
		self.DEPARTAMENTO_COLEGIO_BOYACA,
		self.DEPARTAMENTO_COLEGIO_CALDAS,
		self.DEPARTAMENTO_COLEGIO_CAQUETA,
		self.DEPARTAMENTO_COLEGIO_CASANARE,
		self.DEPARTAMENTO_COLEGIO_CAUCA,
		self.DEPARTAMENTO_COLEGIO_CESAR,
		self.DEPARTAMENTO_COLEGIO_CHOCO,
		self.DEPARTAMENTO_COLEGIO_CUNDINAMARCA,
		self.DEPARTAMENTO_COLEGIO_CORDOBA,
		self.DEPARTAMENTO_COLEGIO_GUAINIA,
		self.DEPARTAMENTO_COLEGIO_GUAVIARE,
		self.DEPARTAMENTO_COLEGIO_HUILA,
		self.DEPARTAMENTO_COLEGIO_GUAJIRA,
		self.DEPARTAMENTO_COLEGIO_MAGDALENA,
		self.DEPARTAMENTO_COLEGIO_META,
		self.DEPARTAMENTO_COLEGIO_NARINO,
		self.DEPARTAMENTO_COLEGIO_NORTE_SANTANDER,
		self.DEPARTAMENTO_COLEGIO_PUTUMAYO,
		self.DEPARTAMENTO_COLEGIO_QUINDIO,
		self.DEPARTAMENTO_COLEGIO_RISARALDA,
		self.DEPARTAMENTO_COLEGIO_SANTANDER,
		self.DEPARTAMENTO_COLEGIO_SUCRE,
		self.DEPARTAMENTO_COLEGIO_TOLIMA,
		self.DEPARTAMENTO_COLEGIO_VALLE,
		self.DEPARTAMENTO_COLEGIO_VAUPES,
		self.DEPARTAMENTO_COLEGIO_VICHADA,
		self.SECTOR_COLEGIO_NO_OFICIAL,
		self.SECTOR_COLEGIO_OFICIAL,
		self.ZONA_COLEGIO_RURAL,
		self.ZONA_COLEGIO_RURAL_URBANA,
		self.ZONA_COLEGIO_URBANA,
		self.ZONA_COLEGIO_URBANA_RURAL,
		self.GENERO_COLEGIO_FEMENINO,
		self.GENERO_COLEGIO_MASCULINO,
		self.GENERO_COLEGIO_MIXTO,
		self.CARACTER_COLEGIO_ACADEMICO,
		self.CARACTER_COLEGIO_NO_APLICA,
		self.CARACTER_COLEGIO_TECNICO,
		self.CARACTER_COLEGIO_TECNICO_ACADEMICO,
		self.CALENDARIO_COLEGIO_A,
		self.CALENDARIO_COLEGIO_B,
		self.CALENDARIO_COLEGIO_OTRO,
		self.CURSO_COLEGIO_NO,
		self.CURSO_COLEGIO_SI,
		self.NACIONALIDAD_CO,
		self.NACIONALIDAD_EX,
		self.GENERO_F,
		self.GENERO_M,
		self.GENERO_N,
		self.ESTADO_CIVIL_CASADO,
		self.ESTADO_CIVIL_DIVORCIADO,
		self.ESTADO_CIVIL_NO_DEFINIDO,
		self.ESTADO_CIVIL_OTRO,
		self.ESTADO_CIVIL_SEPARADO,
		self.ESTADO_CIVIL_SOLTERO,
		self.ESTADO_CIVIL_VIUDO,
		self.ESTRATO_0,
		self.ESTRATO_1,
		self.ESTRATO_2,
		self.ESTRATO_3,
		self.ESTRATO_4,
		self.ESTRATO_5,
		self.ESTRATO_6,
		self.ESTADO_CIVIL_PADRES_CASADOS,
		self.ESTADO_CIVIL_PADRES_DIVORCIADOS,
		self.ESTADO_CIVIL_PADRES_O,
		self.ESTADO_CIVIL_PADRES_SEPARADOS,
		self.ESTADO_CIVIL_PADRES_SIN_INFO,
		self.ESTADO_CIVIL_PADRES_SOLTERO,
		self.ESTADO_CIVIL_PADRES_UNION_LIBRE,
		self.ESTADO_CIVIL_PADRES_VIUDO,
		self.NIVEL_EDU_MADRE_BACHILLERATO,
		self.NIVEL_EDU_MADRE_POSTGRADO,
		self.NIVEL_EDU_MADRE_PRIMARIA,
		self.NIVEL_EDU_MADRE_PROFESIONAL,
		self.NIVEL_EDU_MADRE_SIN_INFO,
		self.NIVEL_EDU_MADRE_TECNICO,
		self.NIVEL_EDU_PADRE_BACHILLERATO,
		self.NIVEL_EDU_PADRE_POSTGRADO,
		self.NIVEL_EDU_PADRE_PRIMARIA,
		self.NIVEL_EDU_PADRE_PROFESIONAL,
		self.NIVEL_EDU_PADRE_SIN_INFO,
		self.NIVEL_EDU_PADRE_TECNICO,
		self.OCUPACION_MADRE_DESEMPLEADA,
		self.OCUPACION_MADRE_EMPLEADA,
		self.OCUPACION_MADRE_EMPRESARIA,
		self.OCUPACION_MADRE_INDEPENDIENTE,
		self.OCUPACION_MADRE_OTRO,
		self.OCUPACION_MADRE_SIN_INFO,
		self.OCUPACION_PADRE_DESEMPLEADA,
		self.OCUPACION_PADRE_EMPLEADA,
		self.OCUPACION_PADRE_EMPRESARIA,
		self.OCUPACION_PADRE_INDEPENDIENTE,
		self.OCUPACION_PADRE_OTRO,
		self.OCUPACION_PADRE_SIN_INFO,
		self.MINORIA_ETNICA_NO,
		self.MINORIA_ETNICA_SIN_INFO,
		self.MINORIA_ETNICA_SI,
		self.DISCAPACIDAD_FISICA_NO,
		self.DISCAPACIDAD_FISICA_SIN_INFO,
		self.DISCAPACIDAD_FISICA_SI
		]]

		# print (inputData,len(inputData[0]),'inputData')

		
		return inputData