from django.urls import path
from . import views

app_name = 'cadastros'

urlpatterns = [
    path('cadastrar/', views.CampoCreate.as_view(), name= 'campo_create' ),
    path('listar/', views.CampoList.as_view(), name= 'campo_list' ),
    path('editar/<int:pk>/', views.CampoUpdate.as_view(), name= 'campo_update' ),
    path('excluir/<int:pk>/', views.CampoDelete.as_view(), name= 'campo_delete' ),
    path('index/', views.PaginaTemplate.as_view(), name= 'pagina_inicial' ),
]
