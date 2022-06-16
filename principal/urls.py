from re import template
from unicodedata import name
from django.urls import path, include
from . import views
#from static import contact, contactar 


#from principal.views import perfilview
from django.contrib.auth.views import LoginView, LogoutView
from principal.views import *


urlpatterns = [
    path('', views.Inicio, name="Form"),
    path('plantilla/', views.plantilla, name="plantilla"),
    path('indexp/', views.indexp, name="indexp"),
    #path('contactar/', views.contactar,name="contactar"),
    #path('', include('django.contrib.auth.urls')),
    path('Registrarse/', views.register, name= 'register'),
    path('Categoria/', views.Categoria, name="Categoria"),
    path('agregar-producto/', views.agregar_Producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('modificar-producto/<int:pk>', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<int:pk>', eliminar_producto, name="eliminar_producto"),
    path('agregar-perfil/', views.editar_Perfil, name="agregar_Perfil"),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/<str:username>/', views.perfil, name='perfil'),
    path('perfilusu/<str:username>/', views.perfilusu, name='perfilusu'),
    path('login/', LoginView.as_view(template_name='registration/Login1.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('agregar-personas/', views.agregar_personas, name="agregar_personas"),
    path('contacto/', views.contacto, name="contacto"),
    path('contacto/<str:username>/', views.contacto, name="contacto"),
    path('verProducto/', views.verProducto, name='verProducto'),
    path('verProducto/<str:username>/', views.verProducto, name='verProducto'),
    path('verProductoo/<int:pk>/', views.verProductoo, name='verProductoo'),
    path('editar_Producto/<int:pk>/', views.editar_Producto, name="editar_Producto"),
    path('cart/',views.cart, name="cart"),
    path('contactar/', views.contactar, name="contactar"),
    path('contact/', views.contact, name="contact"),
    path('calificacionbuena/<str:username>', views.calificacionbuena, name='calificacionbuena'),
    path('calificacionmala/<str:username>', views.calificacionmala, name='calificacionmala'),

 
    #path('CrearProducto/', views.CrearProducto),
    #path('VistaProducto/', views.VistaProducto),
    #path('categoria/', views.ListadoCategoria.as_view(template_name = "categoria/inicio.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
   # path('categoria/detalle/<int:pk>', views.CategoriaDetalle.as_view(template_name = "categoria/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    #path('categoria/crear', views.CategoriaCrear.as_view(template_name = "categoria/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    #path('categoria/editar/<int:pk>', views.CategoriaActualizar.as_view(template_name = "categoria/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    #path('categoria/eliminar/<int:pk>', views.CategoriaEliminar.as_view(), name='categoria/eliminar.html'),    
]
    

   



