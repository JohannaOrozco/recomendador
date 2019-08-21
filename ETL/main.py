import argparse
import logging
logging.basicConfig(level=logging.INFO)
from urllib.parse import urlparse

import pandas as pd
from sklearn.impute import SimpleImputer

# import category_encoders as ce

# import sys
# import csv
# import os

# CLIENT_TABLE = '.clients.csv'
# CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
columns = []

logger = logging.getLogger(__name__)

def main(df):
	logger.info('Run the cleaning')
	# Quitar los estudiantes de intercambio se pierden 1110 registros
	# rows = set(df[df['NOMBRE_PROGRAMA']== 'ESTUDIOS GENER.DE INTERCAMBIO'].index)
	# df = df.drop(rows)

	# Dejar solo el ultimo registro del estudiante por programa
	registros_nuevo_df = listado_indices_ultimo_periodo_programa_estudiante(df)
	df = df.iloc[registros_nuevo_df]
	print (df.shape, ', Shape del DF luego de dejar el ultimo periodo por programa para cada estudiante')


	# Quitar valores atipicos
	df = df.drop(df.index[df['PROMEDIO_ACUMULADO']>5], axis = 0)
	df = df.drop(df.index[df['PROMEDIO_ACUMULADO']== 0], axis = 0)
	df = df.drop(df.index[df['EDAD_INGRESO']<10], axis = 0)
	

	# Salvar registros
	rows = compare_df_columns(df,'NOMBRE_COLEGIO','CLASIFICACION', False)
	df = rows_x_know_column(df, rows, 'NOMBRE_COLEGIO', 'CLASIFICACION', 'PERIODO_GRADO_COLEGIO')
	df['CARACTER_COLEGIO'] = imp_most_frequent(df, 'CARACTER_COLEGIO')
	df['CURSO_COLEGIO'] = imp_most_frequent(df, 'CURSO_COLEGIO')
	df['NACIONALIDAD'] = imp_most_frequent(df, 'NACIONALIDAD')
	columns = ['ESTADO_CIVIL_PADRES', 'NIVEL_EDU_MADRE', 'NIVEL_EDU_PADRE',
				'OCUPACION_MADRE',	'OCUPACION_PADRE',	'MINORIA_ETNICA',
				 'DISCAPACIDAD_FISICA']
	df[columns] = df[columns].fillna('SIN_INFO')
	columns = ['SEGUNDO_PROGRAMA', 'NOMBRE_NOMBRE_FACULTAD',	'NIVEL_SEG_PROG',
				'FACULTAD_DOBLE_PROGR',	'COD_DEPARTAMENTO_SP',	'DEPTO_SEGUNDO_PROGRAMA']
	df[columns] = df[columns].fillna('NO APLICA')

	# Drop Columnas que no agregan valor
	columns = [ 'id_x','ID_PERSONA', 'CODIGO_ESTUDIANTE', 'PROGRAMA_PRIMIPARO', 'PERIODO_PRIMIPARO', 
       			'PERIODO_GRADO_COLEGIO','DEPARTAMENTO_COLEGIO', 'NOMBRE_COLEGIO', 
				'CODIGO_COLEGIO', 'CODIGO_DANE_COLEGIO', 'SNP', 'TIPO_PERIODO', 'CODIGO_FACULTAD',
				'NOMBRE_NOMBRE_FACULTAD', 'NIVEL_PRI_PRO',
				'COD_DEPARTAMENTO', 'DEPARTAMENTO_PROGRAMA', 'SEGUNDO_PROGRAMA',
				'MUNICIPIO_COLEGIO','COD_DEPARTAMENTO_SP', 'TOTAL_HORAS_SEMANA',
				'CURSOS_SEIS_PERIODO', 'CP_CURSOS_DEPARTAMENTO_PROPIO',
				'CP_CURSOS_DEPTO_SEGUNDO_PRO', 'CP_CURSOS_OTRO_DEPARTAMENTO',
				'NIVEL_SEG_PROG', 'FACULTAD_DOBLE_PROGR',
       			'COD_DEPARTAMENTO_SP', 'DEPTO_SEGUNDO_PROGRAMA',
			    'TOTAL_HORAS_SEMANA', 'TOTAL_CURSOS_PERIODO',
			    'NUM_MATERIAS_RETIRADAS', 'NUM_MATERIAS_RETIRADAS_CON_CR',
			    'DOBLE_PROGRAMA', 'DOBLE_PROGRAMA_MISMA_FACULTAD',
			    'NIVEL_DOBLE_PROGRAMA', 'TC_MAGISTRAL', 'TC_LABORATORIO',
			    'TC_ACOMPANAMIENTO', 'TC_EXTRACURRICULAR', 'TC_SECCION_COMPLEMENTARIA',
			    'TC_OTRAS_PRACTICAS', 'TC_PRACTICA_PROFESIONAL', 'TC_PROYECTO_DE_GRADO',
			    'TC_OTROS_PROYECTOS', 'CURSOS_SEIS_PERIODO', 'NC_DOCTORADO',
			    'NC_ESPECIALIZACION', 'NC_MAESTRIA', 'NC_PREGRADO',
			    'NC_NIVELATORIO_POSTGRADO', 'NC_EXTENSION',
			    'CP_CURSOS_DEPARTAMENTO_PROPIO', 'CP_CURSOS_DEPTO_SEGUNDO_PRO',
			    'CP_CURSOS_OTRO_DEPARTAMENTO', 'id_y', 'PERIODO_INGRESO']
			       

	df = df.drop(columns, axis = 1)

	# Drop Columnas por criterio de experto 
	# columns = ['PROGRAMA_PRIMIPARO', 'PERIODO_PRIMIPARO', 'PERIODO_GRADO_COLEGIO',
	# 			'MUNICIPIO_COLEGIO', 'NOMBRE_COLEGIO', 'TIPO_PERIODO',
	# 			'SEGUNDO_PROGRAMA', 'NOMBRE_NOMBRE_FACULTAD', 'NIVEL_SEG_PROG',
	# 			'FACULTAD_DOBLE_PROGR', 'DEPTO_SEGUNDO_PROGRAMA', 'NIVEL_DOBLE_PROGRAMA',
	# 			'DOBLE_PROGRAMA','DOBLE_PROGRAMA_MISMA_FACULTAD','NOMBRE_FACULTAD']

	# df = df.drop(columns, axis = 1)

	# Drop filas con valores nan se pierden 7133 registros
	df = df.dropna()

	# Se cambia el tipo de las Series que estan como numericas pero que son categoricas

	# df['PERIODO_PRIMIPARO'] = df['PERIODO_PRIMIPARO'].astype('str')
	# df['PERIODO'] = df[	'PERIODO'].astype('str')
	# df['PERIODO_GRADO_COLEGIO'] = df['PERIODO_GRADO_COLEGIO'].astype('str')
	df['ESTRATO'] = df['ESTRATO'].astype('str')
	
	#df['CIUDAD_AFUERA'] = df['CIUDAD_AFUERA'].astype('str')
	#df['APOYO_FINANCIERO'] = df['APOYO_FINANCIERO'].astype('str')
	#df['SPP'] = df['SPP'].astype('str')

	# Transformar columnas categoricas

	obj = (df.dtypes == object)
	obj_cols = [c for c in obj.index if obj[c]]
	# Se remueve la variable objetivo
	obj_cols.remove('NOMBRE_PROGRAMA') 
	# obj_cols.remove('NOMBRE_FACULTAD') 

	df = category_get_dummies(df, obj_cols)
	
	# Se revisan las columnas numericas 
	# num = (df.dtypes == float) | (df.dtypes == int)
	# num_cols = [c for c in num.index if num[c]]
	# print (num_cols)

	# 
	print(df.shape)
	print(df.columns)
	_save_data(df, filename)

	return df

def load_file(filename):
	logger.info('Starting cleaning proccess')

	df = _read_data(filename)
	print('df.shape = ', df.shape)


	return df

def _read_data(filename):
	logger.info('Reading file {}'.format(filename))

	return pd.read_csv(filename)

# def _initialize_clients_from_storage():
# 	with open(CLIENT_TABLE, mode='r') as f:
# 		reader = csv.DictReader(f,fieldnames=CLIENT_SCHEMA)

# 		for row in reader:
# 			clients.append(row)


def _save_data(df, filename):
	clean_filename = 'clean_{}'.format(filename)
	logger.info('Saving data at location: {}'.format(clean_filename))
	df.to_csv(clean_filename, index = False)
	return

def category_get_dummies(df, columns):

	for column in columns:
		logger.info('Categori column {}'.format(column))
		df = pd.concat([df,pd.get_dummies(df[column], prefix= column)],axis=1)
		df.drop([column],axis=1, inplace=True)

	return df



def imp_most_frequent(df, column_name):
	logger.info('Imputer the most frecuente value in {}'.format(
		column_name))
	imp_most_frequent = SimpleImputer(strategy='most_frequent')
	df_train = df[[column_name]].dropna()
	imp_most_frequent.fit(df_train)

	values = imp_most_frequent.transform(df[[column_name]])

	X = pd.DataFrame(values)
	X.columns = [column_name]
	X.index = df.index

	X.shape
	return X[column_name]


def compare_df_columns(df,column_notna, column_isna, print_r):
    # Columna notna
    p = set(df[df[column_notna].notna()].index)

    #column_isna
    q = set(df[df[column_isna].isna()].index)

    # Columna de comparación column_notna y column_isna
    if len(p & q) != 0:
        y = len(p & q)
        # print ('En {} se pueden recuperar datos de {}, se encontraron {} registros.'.format(
                    # column_notna, column_isna, y))
        print ('En {} se encontraron {} registros.'.format(
                    column_notna, y))
        r = p & q
        
        if print_r:
            
            print ('Los registros son: {}'.format(r))
        
        return r

def compare_nan_column(df, column_name):        
        cols = list(df.columns)
 
        # Columna base, entonces columna con registros
        #p = set(df[df[column_name].notna()].index)

        # Remover columnas que no se deben revisar
        cols.remove('id')
        cols.remove(column_name)

        for i in cols:
            
            # Columna de comparación, entonces contra columna que no tiene registros
            compare_df_columns(df, i, column_name, False)

def rows_x_know_column(df, rows, know_column, unknow_column, condition_column): #Selección de filas a cambiar con el valor conocido
    rows = set(rows)
    count = 0
    for r in rows:
        
        #print (r, 'fila?')
        value_know = df.loc[r, know_column]
        q = set(df[df[know_column]==value_know].index)
        inter = (rows & q)
        rows = rows - inter
        # Se generó una intersección encuentra el valor la intersección
        if len(inter)>0:
            
            print (inter)
            
            for i in inter:
                
                for qi in q:
                    
                    if int(df[condition_column].loc[i]) == int(df[condition_column].loc[qi]):
                        
                        if str(df[unknow_column].loc[qi]) != 'nan':
                        
                            new_value = str(df[unknow_column].loc[qi])
                            df.loc[i, unknow_column] = new_value
                            count += 1
                            print ('{}- {} {} {}, condición {} {} para la fila {} que estaba {}'.format(count,
                                    str(df[unknow_column].loc[qi]), unknow_column, value_know, 
                                    condition_column, str(df[condition_column].loc[qi]), i, qi))
                            
                            break

    return df

def listado_indices_ultimo_periodo_programa_estudiante(df):
	'Guarda el listado con los indices que tienen el ultimo periodo por programa para cada estudiante'
	registros_nuevo_df = []
	set_estudiantes = set(df['ID_ESTUDIANTE'])

	for estudiante in set_estudiantes:
	    registros_estudiante = df[df['ID_ESTUDIANTE']==estudiante]
	    programas_estudiante = set(registros_estudiante['NOMBRE_PROGRAMA'])

	    for programa_estudiante in programas_estudiante:
	        registros_programa_estudiante = registros_estudiante[registros_estudiante['NOMBRE_PROGRAMA'] == programa_estudiante]
	        periodos_estudiante_programa = registros_programa_estudiante['PERIODO'].values
	        periodos_estudiante_programa.sort()
	        ultimo_periodo = periodos_estudiante_programa[-1]
	        ultimo_periodo
	        registros_nuevo_df.append(
	            registros_estudiante[registros_estudiante['PERIODO']==ultimo_periodo].index.tolist()[0])
	    
	return registros_nuevo_df


# def create_client(client):
# 	global clients

# 	if client not in clients:
# 		clients.append(client)
# 	else:
# 		print ('Client already is in the client\'s list')


# def list_clients():
# 	print ('uid | name | company | email | position')
# 	print ('*' * 50)
# 	for idx, client in enumerate(clients):
# 		print ('{uid} | {name} | {company} | {email} | {position}'.format(
# 			uid = idx,
# 			name = client['name'],
# 			company = client['company'],
# 			email = client['email'],
# 			position = client['position']))


# def update_client(client_id, client_key):
# 	global clients

# 	# if client_name in clients:
# 	# 	index = clients.index(client_name)
# 	# 	clients[index] = updated_client_name
# 	# else:
# 	# 	print('Client is not in clients list')

# 	if client_key in clients[client_id].keys():
# 			clients[client_id][client_key] = input('What the new value? ')
# 	else:
# 		print('Invalid command')


# def _get_client_field_id(client):
# 	global clients
# 	idx = None

# 	while not idx == 'idx':
# 		client = _get_client_field('id')
# 		try:
# 			int(client)
# 			if int(client) < len(clients):
# 				idx = 'idx'
# 			else:
# 				print('client id = {} is not in clients list'.format(client))
# 		except ValueError:
# 			print('Please enter an id number!!! ')
# 	return int(client)


# def delete_client(client):
# 	global clients

# 	clients.pop(client)


# def search_client(client_name):
# 	for client in clients:
# 		if client != client_name:
# 			continue
# 		else:
# 			return True

def _print_welcome():
	print('WELCOME T-Joha CLEAN DATA')
	print('*' * 50)
	# print ('You have loaded the {}'.format(filename))
	# print(df.shape)
	print('What would you like to do today?')
	print('[R]un main process')
	print('[C]ompare_df_columns')
	print('[N]compare_nan_column')
	print('[X]rows_x_know_column')
	# print('[D]elete client')
	print('[S]ave DataFrame in file')

def _get_column_field(field_name):
	field = None

	while not field:
		field = input('What is the column {}? '.format(field_name))

	return field

# def _get_client_field(field_name):
# 	field = None

# 	while not field:
# 		field = input('What is the client {}? '.format(field_name))

# 	return field


# def _get_client_name():
# 	client_name = None

# 	while not client_name:
# 		client_name = input('What is the client name? ')

# 		if client_name == 'exit':
# 			client_name = None
# 			break

# 	if not client_name:
# 		sys.exit()

# 	return client_name

if __name__ == '__main__':
	
	parser = argparse.ArgumentParser()
	parser.add_argument('filename',
	help='The path to the dirty data',
	type= str)

	args = parser.parse_args()

	filename = args.filename

	df = load_file(filename)
	
	_print_welcome()

	command = ''

	while command != 'EXIT':

		command = input()
		command = command.upper()

		if command == 'R':
			main(df)	

		elif command == 'C':

			column_notna = str(_get_column_field('column_notna'))
			column_isna = str(_get_column_field('column_isna'))

			# print (column_notna, '= column_notna',
			# column_isna, '= column_isna')

			rows = compare_df_columns(df, column_notna, column_isna, True)

		elif command == 'N':

			column_name = str(_get_column_field('column_isna'))
			compare_nan_column(df, column_name)

		elif command == 'X':

			# df 
			# rows 
			know_column = str(_get_column_field('know_column'))
			unknow_column = str(_get_column_field('unknow_column'))
			condition_column = str(_get_column_field('condition_column'))
			
			rows_x_know_column(df, rows, know_column, unknow_column, condition_column)
		
		# elif command == 'D':
		# 	list_clients()
		# 	# client_id = int(_get_client_field('id'))
		# 	client_id = _get_client_field_id('id')
		# 	delete_client(client_id)
		# 	list_clients()
		# elif command == 'U':
		# 	list_clients()
		# 	client_id = _get_client_field_id('id')
		# 	client_key = input('What would you like to update name, company, email or pos? ')
		# 	update_client(client_id, client_key)
		# 	list_clients()
		elif command == 'S':
			_save_data(df, filename)
			command = 'EXIT'

		# 	if found:
		# 		print('The client is in the client\'s list')
		# 	else:
		# 		print('The client: {} is not in our client\'s list'.format(client_name)) 
		else:
			print ('If you like exit command = EXIT')
			_print_welcome()
			# command = input()
			# command = command.upper()

		# 

