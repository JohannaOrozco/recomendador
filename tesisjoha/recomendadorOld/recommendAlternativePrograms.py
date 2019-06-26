import pickle
import pandas as pd
import sys

#para quitar los warnings
import warnings
warnings.filterwarnings("ignore")


def main(concepts):
	'Main program'
	
	# Cargar modelos
	loaded_model = load_model('finalized_model_nlp.sav')
	tfidf_model = load_model('finalized_model_tfidf.sav')
	vectorizer_model= load_model('finalized_model_vector.sav')

	# Cargar DataFrame con Programas
	df_programas = load_dataframe('Dataframe_Programas.csv')
	# print (df_programas.head())

	# Cargar datos ingresados por el usuario
	palabras = vectorizer_model.transform([concepts])

	# Correr modelo
	buscador = tfidf_model.transform(palabras)
	distancia,indices       = loaded_model.kneighbors(buscador)


	alternativePrograms = []

	for indice in indices[0]:
		alternativePrograms.append(df_programas.loc[int(indice), 'Programa'])

	# print (alternativePrograms, 'alternativePrograms')
	# print ('It is OK')

	return alternativePrograms


def load_model(url_filename):
	'load model from file'
	filename = url_filename
	loaded_model = pickle.load(open(filename, 'rb'))

	return loaded_model

def load_dataframe(file_path):
	file_path_csv = file_path
	df = pd.read_csv(file_path_csv, sep=',',index_col=0)

	return df


if __name__ == '__main__':
	# main(sys.argv[1])
	main(concepts)


