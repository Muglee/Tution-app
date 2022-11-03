from multiprocessing import context
from pdb import post_mortem
from unicodedata import name
from django.shortcuts import render,HttpResponse
from phonenumbers import supported_calling_codes
from tution.models import Contact
from django.views.generic import TemplateView

def home(request):
    name=['mina','tina']
    context={
        'name':name,
    }
    return render(request,'home.html',context)

class HomeView(TemplateView):
    template_name= 'home.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['msg']="Welcome"
        return context

    
    