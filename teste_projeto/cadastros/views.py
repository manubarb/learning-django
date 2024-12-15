from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from .models import Campo
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, render
from django.conf import settings

class CampoCreate(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    group_required = u"admin"
    login_url = reverse_lazy('login')
    model = Campo
    fields = ['nome', 'descricao', 'arquivo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('cadastros:campo_list')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de itens" 
        context['botao'] = "Cadastrar"
        return context 
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
class CampoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Campo
    template_name = 'cadastros/list.html' 
    
    def get_queryset(self):
        self.object_list = Campo.objects.filter(usuario=self.request.user)
        return self.object_list

class CampoUpdate(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    group_required = u"admin"
    login_url = reverse_lazy('login')
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('cadastros:campo_create')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Campo, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object
    
class CampoDelete(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    group_required = u"admin"
    login_url = reverse_lazy('login')
    model = Campo
    template_name = 'cadastros/excluir.html'
    success_url = reverse_lazy('cadastros:campo_create')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Campo, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

class PaginaTemplate(TemplateView):
        template_name = 'cadastros/index.html'