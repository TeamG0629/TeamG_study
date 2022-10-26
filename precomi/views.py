from django.shortcuts import render
from django.views import generic


#インデックスhtmlに飛ばす
class IndexView(generic.TemplateView):
    template_name = "index.html"
