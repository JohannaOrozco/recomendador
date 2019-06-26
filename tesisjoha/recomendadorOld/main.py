import pickle
# import pandas as pd
# import numpy as np
#from sklearn.preprocessing import StandarScaler
from sklearn.neighbors import KNeighborsClassifier
import recomendadorOld.objects as u
# import recomendadorOld

#para quitar los warnings
import warnings
warnings.filterwarnings("ignore")

# Datos de Prueba

# rawdata = '11,NO OFICIAL,URBANA,MIXTO,ACADEMICO,B,A+,SI,CO,2017,1,80,70,80,,,60,17,N,SOLTERO,4,NO,CASADOS,TECNICO,BACHILLERATO,EMPLEADA,INDEPENDIENTE,NO,NO'


def main(rawdata):
	'Main program'
	
	print ('recibe rawdata: {}'.format(rawdata))
	usuario = u.Usuario(rawdata)
	inputData = usuario.format_data_model()
	recommendedPrograms =recommendPrograms(inputData)
	print (recommendedPrograms, 'recommendedPrograms')

	print ('It is OK')

	return recommendedPrograms


def load_model():
	'load model from file'
	filename = 'recomendadorOld/finalized_model.sav'
	loaded_model = pickle.load(open(filename, 'rb'))
	return loaded_model


def recommendPrograms(inputData):  
	#inputData campos del formulario de entrada separados por ','
	
	# print ("Called python method 'recommendPrograms', with inputData: ",inputData, len(inputData[0]))

	model = load_model()
	resultados = model.predict_proba (inputData)
	resultados_ordenados = sorted(sorted( zip( model.classes_, resultados[0] ), 
			key=lambda x:x[1])[-10:], key=lambda tup:(-tup[1], tup[0]))
	recommendedPrograms = programas_recomendados(3, resultados_ordenados)
	# print (recommendedPrograms, 'recommendedPrograms')
	return recommendedPrograms

def programas_recomendados(n, resultados_ordenados):
	'''Programas recomendados recibe el (n) numero de programas que debe 
	entregar de los resultados ordenados'''
	recommendedPrograms = []
	i = 0
	while i < n:
		recommendedPrograms.append(resultados_ordenados[i][0]+'|'
			+str(resultados_ordenados[i][1]))
		i += 1
	return recommendedPrograms
	



if __name__ == '__main__':
	main(rawdata)