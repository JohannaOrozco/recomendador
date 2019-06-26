from rest_framework.serializers import ModelSerializer

from recomendaciones.models import Estudiante

class EstudianteSerializer(ModelSerializer):

	class Meta:
		model = Estudiante.objects.all()
		fields = ('nombre', 'email')
