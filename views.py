from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.shortcuts import render,render_to_response,get_object_or_404
from dupont.forms import InputForm
from dupont.models import Dupont,Input
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
#from django.views.generic import DetailView
from django.views.generic.edit import FormView,FormMixin
from django.contrib import messages
from django.template import RequestContext
from django.shortcuts import redirect
from django.db.models import Sum,Avg
from django.core.urlresolvers import reverse
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import UpdateView
from django.views.generic.list import ListView
from django.core import serializers



#@csrf_exempt


class DupontView(ListView):
    context_object_name = 'dupont_list'
    template_name = 'dupont_list.html'
    form_class = InputForm
    

    def post(self, request, *args, **kwargs):
        form = InputForm(request.POST)
        if form.is_valid():
            if self.request.is_ajax():
                company = form.cleaned_data['company']
                region = form.cleaned_data['region']
                
                queryset=Result.objects.filter(region=region).aggregate(Sum('sales'))

                return HttpResponse(json.dumps(queryset))
        else:
             return HttpResponse(form.errors)

    def get_queryset(self):
        return Dupont.objects.all()















