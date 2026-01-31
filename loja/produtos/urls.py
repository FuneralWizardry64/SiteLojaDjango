from django.urls import path
from .views import EspeciariaCreate, LivroCreate, QuadroCreate, ArtefatoCreate, LivroUpdate, QuadroUpdate, ArtefatoUpdate, EspeciariaUpdate, EspeciariaDelete, QuadroDelete, ArtefatoDelete, LivroDelete, EspeciariaList, LivroList, ArtefatoList, QuadroList

urlpatterns = [
    path('criar/especiaria', EspeciariaCreate.as_view(), name='criar-especiaria'),
    path('criar/livro', LivroCreate.as_view(), name='criar-livro'),
    path('criar/quadro', QuadroCreate.as_view(), name='criar-quadro'),
    path('criar/artefato', ArtefatoCreate.as_view(), name='criar-artefato'),
    
    path('editar/especiaria/<int:pk>', EspeciariaUpdate.as_view(), name='editar-especiaria'),
    path('editar/livro/<int:pk>', LivroUpdate.as_view(), name='editar-livro'),
    path('editar/quadro/<int:pk>', QuadroUpdate.as_view(), name='editar-quadro'),
    path('editar/artefato/<int:pk>', ArtefatoUpdate.as_view(), name='editar-artefato'),

    path('excluir/especiaria/<int:pk>', EspeciariaDelete.as_view(), name='excluir-especiaria'),
    path('excluir/livro/<int:pk>', LivroDelete.as_view(), name='excluir-livro'),
    path('excluir/quadro/<int:pk>', QuadroDelete.as_view(), name='excluir-quadro'),
    path('excluir/artefato/<int:pk>', ArtefatoDelete.as_view(), name='excluir-artefato'),

    path('listar/especiaria', EspeciariaList.as_view(), name='listar-especiaria'),
    path('listar/livro', LivroList.as_view(), name='listar-livro'),
    path('listar/quadro', QuadroList.as_view(), name='listar-quadro'),
    path('listar/artefato', ArtefatoList.as_view(), name='listar-artefato'),
]