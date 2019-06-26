from django.urls import path

from recomendaciones.views import index, EstudianteAPI, primera_recomendacion, estudiante_view 


# EstudianteCreate,
# from apps.mascota.views import listadousuarios, index, mascota_view, mascota_list, mascota_edit, mascota_delete, \
# 	MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete


urlpatterns = [
    path('index', index, name='index'),
    path('nuevo', estudiante_view, name ='remendacion_crear'),
    # path('nuevo', EstudianteCreate.as_view(), name ='remendacion_crear'),
    path('api', EstudianteAPI.as_view(), name ='api'),
    path('primera_recomendacion', primera_recomendacion, name ='programas'),
    



    # url(r'^nuevo$', login_required(MascotaCreate.as_view()), name='mascota_crear'),
    # url(r'^listar', login_required(MascotaList.as_view()), name='mascota_listar'),
    # url(r'^editar/(?P<pk>\d+)/$', login_required(MascotaUpdate.as_view()), name='mascota_editar'),
    # url(r'^eliminar/(?P<pk>\d+)/$', login_required(MascotaDelete.as_view()), name='mascota_eliminar'),
    # url(r'^listado', listadousuarios, name="listado"),
]