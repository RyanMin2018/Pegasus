# -*- coding: utf-8 -*-
from django.shortcuts import render

# Main Page
def index(request):
    return render(request, 'main/index.html', )