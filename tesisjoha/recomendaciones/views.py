import json
from rest_framework.views import APIView


from django.shortcuts import render, redirect	
from django.http import HttpResponse
# from django.core.urlresolvers import reverse_lazy
from django.urls import reverse_lazy
from django.views.generic import CreateView

from recomendaciones.forms import EstudianteForm
from recomendaciones.models import Estudiante
from recomendaciones.serializers import EstudianteSerializer

import recomendadorOld.main as recommendPrograms


# from django.contrib.auth.models import User

# from django.core import serializers
# from django.core.urlresolvers import reverse_lazy
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# from apps.mascota.forms import MascotaForm
# from apps.mascota.models import Mascota


# # Obtener los datos del formulario
# def contact(request):
# 	if request.method == 'POST': # If the form has been submitted...
# 		form = EstudianteForm(request.POST) # A form bound to the POST data
# 		if form.is_valid(): # All validation rules pass
# 			form.cleaned_data# Process the data in form.cleaned_data
	      
# 			print (form.cleaned_data['my_form_field_name'])
# 			return HttpResponseRedirect('/thanks/') # Redirect after POST
# 	else:
# 		form = EstudianteForm() # An unbound form
# 	return print('Y ahora?')
# 		# render_to_response('recomendaciones/recomendacion_form.html', {
# 		# 'form': form,
# 		# })

# print ('haga algo')
recommendedPrograms = []
# Create your views here.
# def hello_world(request):
# 	'Return a greeting'
# 	return HttpResponse('NUEVO TEXTO!')

def estudiante_view(request):
	if request.method == 'POST':
		form = EstudianteForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			print (data,'TRATANDO CON OTRA COSAAAAAAAA')
			field = data['email']
			print (field,'EMAIL')
			# Probando la llamada al recomendador
			recommendedPrograms = recommendPrograms.main('11,NO OFICIAL,URBANA,MIXTO,ACADEMICO,B,A+,SI,CO,2017,1,80,70,80,,,60,17,N,SOLTERO,4,NO,CASADOS,TECNICO,BACHILLERATO,EMPLEADA,INDEPENDIENTE,NO,NO')
			print ('ESTAMOS MAS CERCA', recommendedPrograms)

		return render(request, 'recomendaciones/primera_recomendacion.html', {'content' : 'SOY EL CONTENIDO {}'.format(recommendedPrograms)})

			# form.save()
		# return render(request, 'programa', {'form' : form})
	else:
		form = EstudianteForm()

	return render(request, 'recomendaciones/recomendacion_form.html', {'form' : form})



def index(request):
	model = Estudiante
	print (model.cleaned_data, 'model')
	# data = request.POST.copy()
	# # print (EstudianteCreate.data (request))

	# print ('HOLA JAHIR')
	# # estudiante = EstudianteCreate()
	# # print (estudiante.email)
	# # contact(request)
	return render(request, 'recomendaciones/index.html')

def primera_recomendacion(request):
	print ('Aqui debe ir el resto del código')

	return render(request, 'recomendaciones/primera_recomendacion.html', {'content' : 'SOY EL CONTENIDO {}'.format(recommendedPrograms)})


# class EstudianteCreate(CreateView):

# 	model = Estudiante
# 	form_class = EstudianteForm
# 	template_name = 'recomendaciones/recomendacion_form.html'
# 	success_url = reverse_lazy('index')

# 	# def primera_recomendacion(request):
# 	# 	print ('Aqui debe ir el resto del código')
# 	# 	data = form.cleaned_data
# 	# 	print (data,'TRATANDO CON OTRA COSAAAAAAAA')
# 	# 	field = data['email']
# 	# 	print (field,'EMAIL')
# 	# 	# Probando la llamada al recomendador
# 	# 	recommendedPrograms = recommendPrograms.main('11,NO OFICIAL,URBANA,MIXTO,ACADEMICO,B,A+,SI,CO,2017,1,80,70,80,,,60,17,N,SOLTERO,4,NO,CASADOS,TECNICO,BACHILLERATO,EMPLEADA,INDEPENDIENTE,NO,NO')
# 	# 	print ('ESTAMOS MAS CERCA', recommendedPrograms)

# 	# 	return render(request, 'recomendaciones/primera_recomendacion.html', {'content' : 'SOY EL CONTENIDO {}'.format(recommendedPrograms)})

# 	def estudiante_view(self, request, form):

# 		data = form.cleaned_data
# 		print (data,'TRATANDO CON OTRA COSAAAAAAAA')
# 		field = data['email']
# 		print (field,'EMAIL')
# 		print ('SE IMPRIME')
# 		if request.method == 'POST':
# 			form = EstudianteForm(request.POST)
# 			if form.is_valid():
# 				form.save()
# 			return redirect('index')
# 		else:
# 			form = EstudianteForm()
	
# 		return render(request, 'recomendaciones/recomendacion_form.html', {'form' : form})

# def recomendacion_list(request):


	# def form_valid(self, form):
	# 	# print('Me estoy imprimiendo {}'.format (form))

	# 	data = form.cleaned_data
	# 	print (data,'TRATANDO CON OTRA COSAAAAAAAA')
	# 	field = data['email']
	# 	print (field,'EMAIL')
	# 	# Probando la llamada al recomendador
	# 	recommendedPrograms = recommendPrograms.main('11,NO OFICIAL,URBANA,MIXTO,ACADEMICO,B,A+,SI,CO,2017,1,80,70,80,,,60,17,N,SOLTERO,4,NO,CASADOS,TECNICO,BACHILLERATO,EMPLEADA,INDEPENDIENTE,NO,NO')
	# 	print ('ESTAMOS MAS CERCA', recommendedPrograms)
	# 	# print (self.model.email,'TRATANDO CON OTRA COSA')

	# 	# return render(request, 'recomendaciones/primera_recomendacion.html', {'content' : 'SOY EL CONTENIDO {}'.format(recommendedPrograms)})

	# 	return super().form_valid(form)



 #        # This method is called when valid form data has been POSTed.
 #        # It should return an HttpResponse.
 #        # form.send_email()
 		# return super().form_valid(form)

	# def imprimir ():
	# 	print (self.model, 'MODEL')

class EstudianteAPI(APIView):
	serializer = EstudianteSerializer

	def get(self, request, format=None):
		lista = Estudiante
		response = self.serializer(lista, many = True)

		print ('llamando la API')

		return HttpResponse(json.dumps(response.data), content_type = 'application/json')





	


# class MascotaUpdate(UpdateView):
# 	model = Mascota
# 	form_class = EstudianteForm
# 	template_name = 'recomendaciones/recomendacion_form.html'
# 	success_url = reverse_lazy('recomendaciones:mascota_listar')


# def estudiante_view(request):
# 	if request.method == 'POST':
# 		form = EstudianteForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 		return redirect('index')
# 	else:
# 		form = EstudianteForm()

# 	return render(request, 'recomendaciones/recomendacion_form.html', {'form' : form})

# def recomendacion_list(request):

# 	pass



# def listadousuarios(request):
# 	lista = serializers.serialize('json', User.objects.all(), fields=['username', 'first_name'])
# 	return HttpResponse(lista, content_type='application/json')

# def index(request):
# 	return render(request, 'mascota/index.html')


# def mascota_view(request):
# 	if request.method == 'POST':
# 		form = MascotaForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 		return redirect('mascota:mascota_listar')
# 	else:
# 		form = MascotaForm()
# 	return render(request, 'mascota/mascota_form.html', {'form':form})


# def mascota_list(request):
# 	mascota = Mascota.objects.all().order_by('id')
# 	contexto = {'mascotas':mascota}
# 	return render(request, 'mascota/mascota_list.html', contexto)



# def mascota_edit(request, id_mascota):
# 	mascota = Mascota.objects.get(id=id_mascota)
# 	if request.method == 'GET':
# 		form = MascotaForm(instance=mascota)
# 	else:
# 		form = MascotaForm(request.POST, instance=mascota)
# 		if form.is_valid():
# 			form.save()
# 		return redirect('mascota:mascota_listar')
# 	return render(request, 'mascota/mascota_form.html', {'form':form})



# def mascota_delete(request, id_mascota):
# 	mascota = Mascota.objects.get(id=id_mascota)
# 	if request.method == 'POST':
# 		mascota.delete()
# 		return redirect('mascota:mascota_listar')
# 	return render(request, 'mascota/mascota_delete.html', {'mascota':mascota})


# class MascotaList(ListView):
# 	model = Mascota
# 	template_name = 'mascota/mascota_list.html'
# 	paginate_by = 2




# class MascotaUpdate(UpdateView):
# 	model = Mascota
# 	form_class = EstudianteForm
# 	template_name = 'recomendaciones/recomendacion_form.html'
# 	success_url = reverse_lazy('recomendaciones:mascota_listar')


# class MascotaDelete(DeleteView):
# 	model = Mascota
# 	template_name = 'mascota/mascota_delete.html'
# 	success_url = reverse_lazy('mascota:mascota_listar')