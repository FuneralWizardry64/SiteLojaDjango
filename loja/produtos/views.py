from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Especiaria, Artefato, Quadro, Livro
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
# Create your views here.

class EspeciariaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Gerenciador"
    model = Especiaria
    fields = ['nome','valor','disponibilidade','descricao']
    template_name = 'produtos/form.html'
    success_url = reverse_lazy('listar-especiaria')
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"
        return context


class ArtefatoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Gerenciador"
    model = Artefato
    fields = ['nome','valor','disponibilidade','descricao','tipo']
    template_name = 'produtos/form.html'
    success_url = reverse_lazy('listar-artefato')
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"
        return context


class QuadroCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Gerenciador"
    model = Quadro
    fields = ['nome','valor','disponibilidade','descricao','autor']
    template_name = 'produtos/form.html'
    success_url = reverse_lazy('listar-quadro')
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"
        return context


class LivroCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Gerenciador"
    model = Livro
    fields = ['nome','valor','disponibilidade','descricao','isbn']
    template_name = 'produtos/form.html'
    success_url = reverse_lazy('listar-livro')
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"
        return context

class EspeciariaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Funcionario", u"Gerenciador"
    model = Especiaria
    fields = ['nome','valor','disponibilidade','descricao']
    template_name = 'produtos/form.html'
    success_url = reverse_lazy('listar-especiaria')
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"
        return context

class ArtefatoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Funcionario", u"Gerenciador"
    model = Artefato
    fields = ['nome', 'valor', 'disponibilidade', 'descricao', 'tipo']
    template_name = 'produtos/form.html'
    success_url = reverse_lazy('listar-artefato')
    login_url = reverse_lazy('inicio')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"
        return context

class QuadroUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Funcionario", u"Gerenciador"
    model = Quadro    
    fields = ['nome','valor','disponibilidade','descricao','autor']
    template_name = 'produtos/form.html'
    success_url = reverse_lazy('listar-quadro')
    login_url = reverse_lazy('inicio')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"
        return context

class LivroUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Funcionario", u"Gerenciador"
    model = Livro
    fields = ['nome','valor','disponibilidade','descricao','isbn']
    template_name = 'produtos/form.html'
    success_url = reverse_lazy('listar-livro')
    login_url = reverse_lazy('inicio')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"
        return context

class EspeciariaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Gerenciador", u"Gerenciador"
    model = Especiaria
    template_name = 'produtos/excluir.html'
    success_url = reverse_lazy('listar-especiaria')
    login_url = reverse_lazy('inicio')

    

class ArtefatoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Gerenciador", u"Gerenciador"
    model = Artefato
    template_name = 'produtos/excluir.html'
    success_url = reverse_lazy('listar-artefato')
    login_url = reverse_lazy('inicio')

class QuadroDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Gerenciador", u"Gerenciador"
    model = Quadro
    template_name = 'produtos/excluir.html'
    success_url = reverse_lazy('listar-quadro')
    login_url = reverse_lazy('inicio')

class LivroDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Gerenciador", u"Gerenciador"
    model = Livro
    template_name = 'produtos/excluir.html'
    success_url = reverse_lazy('listar-livro')
    login_url = reverse_lazy('inicio')

class EspeciariaList(ListView):
    model = Especiaria
    template_name = 'produtos/lista/especiaria.html'

class ArtefatoList(ListView):
    model = Artefato
    template_name = 'produtos/lista/artefato.html'

class QuadroList(ListView):
    model = Quadro
    template_name = 'produtos/lista/quadro.html'

class LivroList(ListView):
    model = Livro
    template_name = 'produtos/lista/livro.html'
