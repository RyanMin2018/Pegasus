# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import CreateUserForm
from django.core.urlresolvers import reverse_lazy

class CreateUserView(CreateView):
    template_name = 'registration/join.html'
    form_class    = CreateUserForm
    success_url   = reverse_lazy('join_complete')

class RegisteredView(TemplateView):
    template_name = 'registration/join_complete.html'