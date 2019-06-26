import sys


# rawdata = 'Licenciatura en Matemáticas, Ingeniería Biomédica, Ingeniería Industrial'

dictionary_concepts_programs = {'Arquitectura' : ['enseñanza', 'arquitectura', 'ciudad', 'responsabilidad', 'producción'],
								'Literatura' : ['literatura', 'atención', 'disciplinar', 'hispánico', 'tradición'],
								'Física' : ['interés', 'mentalidad', 'física', 'método', 'principio'],
								'Licenciatura en Humanidades' : ['relación', 'texto', 'humanidades', 'elección', 'interpretación'],
								'Medicina' : ['médico', 'principio', 'sociedad', 'colega', 'aproximación'],
								'Licenciatura en Matemáticas' : ['matemáticas', 'licenciatura', 'proyecto', 'evaluador', 'diseñador'],
								'Ingeniería Biomédica' : ['biomédico', 'ingeniero', 'farmacéuticos', 'hospitales', 'equipar'],
								'Ingeniería Industrial' : ['industrial', 'producción', 'gestión', 'empresa', 'ingeniería'],
								'Gobierno y Asuntos Públicos': ['sector', 'gestión', 'asuntos', 'públicos', 'gobierno'],
								'Ingeniería Electrónica' : ['sistema', 'servicio', 'electrónico', 'ingeniero', 'tratamiento'],
								'Contaduría Internacional' : ['organización', 'contaduría', 'internacional', 'estándar', 'negocio'],
								'Psicología' : ['psicología', 'psicólogo', 'universidad', 'prestigiar', 'aporte'],
								'Administración' : ['administración', 'personar', 'estudiante', 'oportunidad', 'organización'],
								'Geociencias' : ['geocientífico', 'geocientíficos', 'necesidad', 'recurso', 'ambientar'],
								'Economía' : ['economía', 'público', 'cargo', 'nivel', 'sector'],
								'Música' : ['músico', 'composición', 'práctico', 'cámara', 'cine'],
								'Lenguas y Cultura' : ['lengua', 'campar', 'formación', 'culturales', 'perfil'],
								'Licenciatura en Educación para la Primera Infancia' : ['educación', 'año', 'infancia', 'primera', 'licenciado'],
								'Química' : ['interés', 'teoría', 'proceso', 'conocimiento', 'entorno'],
								'Biología' : ['ciencia', 'nivel', 'buscar', 'biología', 'sólido'],
								'Ingeniería Química' : ['ingeniería', 'química', 'producto', 'proceso', 'procesar'],
								'Derecho' : ['nación', 'abogado', 'general', 'habilidad', 'formar'],
								'Ciencia Política' : ['interesar', 'ciencia', 'gubernamentales', 'rama', 'politólogos'],
								'Ingeniería de Sistemas y Computación' : ['sistema', 'computación', 'sistemas', 'calidad', 'información'],
								'Ingeniería Mecánica' : ['actividad', 'ingeniería', 'profesional', 'mecánica', 'cabo'],
								'Microbiología' : ['producto', 'control', 'microbiología', 'mejoramiento', 'aspecto'],
								'Historia' : ['historia', 'gestión', 'docencia', 'universidad', 'recuperación'],
								'Licenciatura en Ciencias Naturales' : ['ciencia', 'currículo', 'joven', 'aula', 'adulto'],
								'Licenciatura en Ciencias Sociales' : ['competencia', 'sociales', 'profundización', 'ciencias', 'filosofía'],
								'Ingeniería Eléctrica' : ['telecomunicación', 'sector', 'sistema', 'servicio', 'eléctrico'],
								'Arte' : ['arte', 'contexto', 'medio', 'espacio', 'pregrado'],
								'Licenciatura en Artes' : ['licenciados', 'artes', 'experiencia', 'situación', 'estudiante'],
								'Historia del Arte' : ['arte', 'historia', 'museo', 'historiador', 'profesor'],
								'Diseño' : ['contemporaneidad', 'creatividad', 'entornar', 'diseño', 'ideación'],
								'Filosofía' : ['filosofía', 'formación', 'egresar', 'publicidad', 'pensador'],
								'Antropología' : ['antropología', 'análisis', 'arqueología', 'recolección', 'antropólogo'],
								'Ingeniería Ambiental' : ['ambiental', 'empresa', 'ingeniero', 'ingeniería', 'capacidad'],
								'Matemáticas' : ['alguno', 'matemáticas', 'docencia', 'país', 'estudio'],
								'Ingeniería Civil' : ['civil', 'empresa', 'ingeniero', 'ingeniería', 'proyecto']}

def main(rawdata):
	'Main program'

	programs = my_string(rawdata)
	concepts = findConcepts(programs)
	print (concepts)
	return concepts


def my_string(rawdata):
	'take a rawdata to transform in list'

	my_string = rawdata
	result = [x.strip() for x in my_string.split(',')]

	return result



def findConcepts(programs):
	'Find concepts asociate with the program'
	# print ("Called python method 'findConcepts', with inputData: ", programs)
	concepts = []

	for program in programs:
	
		for concept in dictionary_concepts_programs[program]:
			concepts.append(concept)

	return concepts



if __name__ == '__main__':
	main(rawdata)
	# main(sys.argv[1])