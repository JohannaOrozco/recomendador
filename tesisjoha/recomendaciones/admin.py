from django.contrib import admin

from recomendaciones.models import Estudiante, ColegioClasificacion, EstudianteNacionalidad, EstudianteGenero, EstudianteEstadoCivil, EstudianteEstrato, EstudianteTieneFinanciacion, EstudiantePerteneceMinoriaEtnica, EstudianteTieneDiscapacidad

# Register your models here.
admin.site.register(Estudiante)
admin.site.register(EstudianteNacionalidad)
admin.site.register(EstudianteGenero)
admin.site.register(EstudianteEstadoCivil)
admin.site.register(EstudianteEstrato)
admin.site.register(EstudianteTieneFinanciacion)
admin.site.register(EstudiantePerteneceMinoriaEtnica)
admin.site.register(EstudianteTieneDiscapacidad)


admin.site.register(ColegioClasificacion)
