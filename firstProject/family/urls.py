from django.urls import path
from django.conf.urls.static import static
from myHome import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('template/', views.template, name='template'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


