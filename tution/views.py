from distutils.command.clean import clean
from msilib.schema import ListView
from multiprocessing import context
from re import template
from unittest import result
from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact,Post
from .forms import ContactForm, PostForm
from django.views import View
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.db.models import Q
def search(request):
    query=request.POST.get('search','')
    if query:
        queryset=(Q(title__icontains=query)) | (Q(details__icontains=query)) | (Q(medium__icontains=query)) | (Q(category__icontains=query))
        result=Post.objects.filter(queryset).distinct()
    else:
        results=[]
    context={
        'results':results
    }  
    return render(request,'tution/search.html',context)  


class ContactView(FormView):
    form_class=ContactForm
    template_name='contact.html'
    success_url='/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    def form_invalid(self, form):
        return super().form_invalid(form)
    def get_success_url(self):
        return reverse_lazy('homeview')
# class ContactView(View):
#     form_class=ContactForm
#     template_name='contact.html'
#     def get(self,request,*args, **kwargs):
#         form=self.form_class()
#         return render(request,self.template_name,{'form':form})

#     def post(self,request,*args, **kwargs):
#         form=self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("success")
#         return render(request,self.template_name,{'form':form})
# Create your views here.
def contact(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ContactForm()
    return render(request,'contact.html',{'form':form})

from django.views.generic import ListView
class PostListView(ListView):
    template_name='tution/postlist.html'
    queryset=Post.objects.all()
    context_object_name='posts'
    def get_context_data(self, *args, **kwargs):
        context=super().get_context_data( *args,**kwargs)
        context['posts']=context.get('object_list')
        context['msg']='This is post list'
        return context

from django.views.generic import DetailView
class PostDetailView(DetailView):
    model=Post
    template_name='tution/postdetail.html'
    def get_context_data(self, *args, **kwargs):
        context=super().get_context_data( *args,**kwargs)
        context['post']=context.get('object')
        context['msg']='This is post list'
        return context
def postview(request):
    post=Post.objects.all()
    return render(request,'tution/postview.html',{'post':post})

from django.views.generic import CreateView
class PostCreateView(CreateView):
    model=Post
    form_class=PostForm
    template_name= 'tution/postcreate.html'
    success_url='/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        # id= self.object.id
        return reverse_lazy('tution:subjects')

from django.views.generic import UpdateView,DeleteView
class PostEditView(UpdateView):
    model=Post
    form_class=PostForm
    template_name= 'tution/postcreate.html'
    def get_success_url(self):
        id= self.object.id
        return reverse_lazy('tution:postdetail',kwargs={'pk':id})
class PostDeleteView(DeleteView): 
    model=Post
    template_name='tution/delete.html'
    success_url=reverse_lazy('tution/postlist')
def postcreate(request):
    if request.method=="POST":
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            sub=form.cleaned_data['subject']
            for i in sub:
                obj.subject.add(i)
                obj.save()
            class_in=form.cleaned_data['class_in']
            for i in class_in:
                obj.class_in.add(i)
                obj.save()
            return HttpResponse("Success")
    else:
        form=PostForm()
    return render(request,'tution/postcreate.html',{'form':form})
